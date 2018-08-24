# -*- coding: utf-8 -*-

from __future__ import absolute_import
from behave.formatter.base import Formatter


class MiniFormatter(Formatter):
    """
    Provides a simple plain formatter without coloring/formatting.
    The formatter displays only scenario name
    """
    name = "plain"
    description = "Very basic formatter with maximum compatibility"

    SHOW_MULTI_LINE = False
    SHOW_TAGS = False
    SHOW_ALIGNED_KEYWORDS = False
    indent_size = 0
    RAISE_OUTPUT_ERRORS = True

    def scenario(self, scenario):
        text = u"%s: %s" % (scenario.keyword, scenario.name)
        self.stream.write(text)
        self.stream.write(u"\n")
