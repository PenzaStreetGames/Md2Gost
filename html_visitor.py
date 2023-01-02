class HtmlTreeVisitor:

    def __init__(self):
        pass

    def visit(self, node):
        if type(node) == list:
            return [self.visit(node_item) for node_item in node]
        if type(node) != dict:
            return
        if "type" not in node:
            return
        node_type = node["type"]
        visit_method_name = f"_visit_{node_type}"
        children_res = None
        if 'children' in node:
            children_res = [self.visit(child) for child in node['children']]
        if hasattr(self, visit_method_name) and callable(getattr(self, visit_method_name)):
            return getattr(self, visit_method_name)(node, children_res)
        else:
            return f"<b style='color: red;'>no such visit method {visit_method_name}</b>"

    def _visit_heading(self, node, children_res):
        level = node["attrs"]["level"]
        inner = "".join(children_res)
        return f"<h{level}>{inner}</h{level}>"

    def _visit_text(self, node, children_res):
        return node["raw"]

    def _visit_blank_line(self, node, children_res):
        return "\n"

    def _visit_paragraph(self, node, children_res):
        inner = " ".join(children_res)
        return f"{inner}"

    def _visit_block_code(self, node, children_res):
        text = node["raw"]
        return f'<pre>\n{text}</pre>\n'

    def _visit_softbreak(self, node, children_res):
        return ""

    def _visit_link(self, node, children_res):
        inner = "".join(children_res)
        url = node["attrs"]["url"]
        return f'<a href="{url}">{inner}</a>'

    def _visit_codespan(self, node, children_res):
        text = node["raw"]
        return f'<code>{text}</code>'

    def _visit_strikethrough(self, node, children_res):
        inner = "".join(children_res)
        return f'<del>{inner}</del>'

    def _visit_table(self, node, children_res):
        inner = "\n".join(children_res)
        return f'<table style="border: 1px solid black; border-collapse: collapse;">\n{inner}\n</table>\n'

    def _visit_table_head(self, node, children_res):
        inner = "\n".join(children_res)
        return f'<thead>\n{inner}\n</thead>\n'

    def _visit_table_body(self, node, children_res):
        inner = "\n".join(children_res)
        return f'<tbody>\n{inner}\n</tbody>\n'

    def _visit_table_row(self, node, children_res):
        inner = "\n".join(children_res)
        return f'<tr>\n{inner}\n</tr>\n'

    def _visit_table_cell(self, node, children_res):
        inner = ''.join(children_res)
        return f'<td style="border: 1px solid black; border-collapse: collapse;">{inner}</td>'

    def _visit_list(self, node, children_res):
        inner = '\n'.join(children_res)
        list_type = 'ol' if node['attrs']['ordered'] else 'ul'
        return f'<{list_type}>\n{inner}\n</{list_type}>'

    def _visit_list_item(self, node, children_res):
        inner = ''.join(children_res)
        return f'<li>{inner}</li>'

    def _visit_image(self, node, children_res):
        alt = ''.join(children_res)
        url = node['attrs']['url']
        return f'<br><img src="{url}" alt="{alt}"><br>'

    def _visit_block_text(self, node, children_res):
        inner = ' '.join(children_res)
        return f'<p>{inner}</p>'

    def _visit_emphasis(self, node, children_res):
        inner = ' '.join(children_res)
        return f'<i>{inner}</i>'

    def _visit_strong(self, node, children_res):
        inner = ' '.join(children_res)
        return f'<b>{inner}</b>'

    def _visit_inline_math(self, node, children_res):
        inner = node['raw']
        return f'$${inner}$$'