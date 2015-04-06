#!/usr/bin/env python3

"""Nice use of format function"""

import math

constants = "Math constants: pi={m.pi:.3f}, e={m.e:.4f}".format(m=math)
print(constants)
