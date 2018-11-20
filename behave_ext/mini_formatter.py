# -*- coding: utf-8 -*-
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
