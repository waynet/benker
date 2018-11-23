# coding: utf-8
"""
Base Parser
===========

Base class of parsers.
"""
from lxml import etree


class BaseParser(object):
    """
    Abstract base class of the parsers classes.
    """

    def __init__(self, builder, **options):
        """
        Construct a base builder.

        :type  builder: benker.builders.base_builder.BaseBuilder
        :param builder:
            Builder used by this parser to instantiate :class:`~benker.table.Table` objects.

        :param str options: Extra conversion options.
        """
        self.builder = builder
        self.options = options

    def parse_file(self, src_xml, dst_xml):
        tree = etree.parse(src_xml)
        self.transform_tables(tree)
        encoding = self.options.get('encoding', 'utf-8')
        tree.write(dst_xml, encoding=encoding, pretty_print=False)

    def transform_tables(self, tree):
        raise NotImplementedError


def value_of(element, xpath, namespaces=None, default=None):
    """
    Take the first value of a xpath evaluation.

    :type  element: etree._Element
    :param element: Root element used to evaluate the xpath expression.

    :param str xpath: xpath expression.
        This expression will be evaluated using the :data:`NS` namespace.

    :type  namespaces: dict[str, str]
    :param namespaces:
        Namespace map to use for the xpath evaluation.

    :param default: default value used if the xpath evaluation returns no result.

    :return: the first result or the *default* value.
    """
    nodes = element.xpath(xpath, namespaces=namespaces)
    return nodes[0] if nodes else default
