# -*- coding: utf-8 -*-
from behave.formatter.base import Formatter


class Mini(Formatter):
    """
    Provides a simple plain formatter without coloring/formatting.
    The formatter displays only scenario name
    """

    description = "Print out only scenario titles"

    DEFAULT_INDENT_SIZE = 0
    RAISE_OUTPUT_ERRORS = True
    SHOW_ALIGNED_KEYWORDS = False
    SHOW_BACKGROUNDS = False
    SHOW_MULTI_LINE = False
    SHOW_RULES = False
    SHOW_TAGS = False
    SHOW_SUMMARY = False

    def scenario(self, scenario):
        skip_config_tags = [
            tag.replace("-", "")
            for tag in str(self.config.tags).split()
            if tag.startswith("-")
        ]
        has_feature_skip_tags = any(
            skip_tag in scenario.feature.tags for skip_tag in skip_config_tags
        )
        has_scenario_skip_tags = any(
            skip_tag in scenario.tags for skip_tag in skip_config_tags
        )
        if not has_scenario_skip_tags and not has_feature_skip_tags:
            self.stream.write(f"{scenario.name}\n")
