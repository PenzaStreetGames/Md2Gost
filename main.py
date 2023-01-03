import docx

import json
import mistune
from html_visitor import HtmlTreeVisitor
from docx_visitor import DocxTreeVisitor


def dump_html(md_tree: dict):
    html_tree_visitor = HtmlTreeVisitor()
    with open('html/article.html', 'w', encoding='utf-8') as outfile:
        header = '''
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
'''
        outfile.write(header + "".join(html_tree_visitor.visit(md_tree)))


def dump_docx(md_tree: dict):
    docx_tree_visitor = DocxTreeVisitor()
    docx_tree_visitor.visit(md_tree)
    docx_tree_visitor.doc.save('docx/article.docx')


if __name__ == '__main__':
    with open("habr.md", "r", encoding="utf-8") as infile:
        md = infile.read()
    markdown = mistune.create_markdown(renderer=None, plugins=['table', 'url', 'math', 'strikethrough'])
    with open("json/mistune.json", "w", encoding="utf-8") as outfile:
        outfile.write(json.dumps(markdown(md), indent=2))
    md_tree: dict = markdown(md)
    # dump_html(md)
    dump_docx(md_tree)


