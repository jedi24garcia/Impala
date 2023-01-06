#!/usr/bin/env python3

import numpy as np

# creating basic array
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a[0])


# not related at all
# allclose()function
a = np.array([0.16,0.26,0.365])
b = np.array([0.15,0.25,0.36])
tolerance1 = 0.1
tolerance2 = 0.05
print(np.allclose(a,b,tolerance1))
print(np.allclose(a,b,tolerance2))
