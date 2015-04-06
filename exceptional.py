'''A module for demonstrating exceptions'''

import sys
from math import log

def convert(s):
    '''Convert to an integer.'''
    try:
        x = int(s)
        print("Conversion succeeded! x = ", x)
    except(ValueError, TypeError) as e:
        print("Conversion error: {}".format(str(e)), file = sys.stderr)
        print("Conversion failed!")
        x = -1 # Better to use raise to propagate the exception
        raise
    return x

def string_log(s):
    v = convert(s)
    return log(v)
