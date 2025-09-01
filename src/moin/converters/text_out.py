# Copyright: 2011 MoinMoin:ThomasWaldmann
# License: GNU GPL v2 (or any later version), see LICENSE.txt for details.

"""
MoinMoin - Plain text output converter.

Convert an internal document tree into plain, unformatted text.

The purpose of this converter is mainly to be used in a converter chain like
markup -> DOM -> text to get rid of the (wiki, reStructuredText, DocBook, ...) markup;
thus we get indexable plain text for our search index.
"""

from . import default_registry
from moin.utils.mime import type_moin_document, type_text_plain


class Converter:
    """
    Converter application/x.moin.document -> text/plain
    """

    @classmethod
    def factory(cls, input, output, **kw):
        return cls()

    def __call__(self, root):
        return "\n".join(root.itertext())


default_registry.register(Converter.factory, type_moin_document, type_text_plain)
