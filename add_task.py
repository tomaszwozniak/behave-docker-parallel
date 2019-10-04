# -*- coding: utf-8 -*-
import sys

from tasks import delegate_test


def main(browser: str, scenario: str):
    delegate_test.delay(browser, scenario)


if __name__ == "__main__":
    main(browser=sys.argv[1], scenario=sys.argv[2])
