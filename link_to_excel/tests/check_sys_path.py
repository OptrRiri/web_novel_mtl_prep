import sys, os
from pprint import pprint
from ..vars import selenium_configs

def test():
    sys.path.append(selenium_configs.local_relative_geckodriver_pathStr)
    pprint(sys.path)
    pprint(os.environ['PATH'])

if __name__ == "__main__":
    test()