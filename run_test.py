import sys

from tasks import delegate_test


def main(scenario):
    delegate_test.delay(scenario)


if __name__ == '__main__':
    main(sys.argv[1])
