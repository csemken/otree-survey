from docutils import nodes
from docutils.parsers.rst.directives.admonitions import Note, BaseAdmonition
from docutils.parsers.rst.directives.body import Container
from sphinx.builders.latex import LaTeXBuilder
from sphinx.util.docutils import SphinxDirective


class howto(nodes.Admonition, nodes.Element):
    pass


def visit_howto(self, node):
    self.visit_admonition(node)
    if not isinstance(node[0], nodes.title):
        node.insert(0, nodes.title("howto", "How to do it"))


def depart_howto(self, node):
    self.depart_admonition(node)


class HowtoDirective(BaseAdmonition, SphinxDirective):
    node_class = howto

    def run(self):
        if type(self.env.app.builder) == LaTeXBuilder:
            return []
        return BaseAdmonition.run(self)


class PubOnlyDirective(Container, SphinxDirective):
    optional_arguments = 0

    def run(self):
        if type(self.env.app.builder) != LaTeXBuilder:
            return []
        return Container.run(self)


class DocOnlyDirective(Container, SphinxDirective):
    optional_arguments = 0

    def run(self):
        if type(self.env.app.builder) == LaTeXBuilder:
            return []
        return Container.run(self)


def setup(app):
    app.add_node(
        howto, html=(visit_howto, depart_howto), latex=(visit_howto, depart_howto)
    )
    app.add_directive("howto", HowtoDirective)
    app.add_directive("pubonly", PubOnlyDirective)
    app.add_directive("doconly", DocOnlyDirective)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
