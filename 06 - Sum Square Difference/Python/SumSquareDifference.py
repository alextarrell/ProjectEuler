#! /usr/bin/env python
#Problem 6 Euler

import numpy as np

print np.sum(np.arange(1,101)) ** 2 - np.sum(np.square(np.arange(1,101)))
