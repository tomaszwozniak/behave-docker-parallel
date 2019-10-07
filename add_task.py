# -*- coding: utf-8 -*-
import sys

from tasks import delegate_test

if __name__ == "__main__":
    delegate_test.delay(browser=sys.argv[1], scenario=sys.argv[2])
