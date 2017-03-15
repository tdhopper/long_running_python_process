import logging
import sys
import itertools
import time


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


if __name__ == '__main__':
    for iteration in itertools.count(start=1):
        logging.info("Process ran for the {}th time".format(iteration))
        time.sleep(30)
