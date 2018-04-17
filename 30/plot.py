#!/usr/bin/env python3

import math
import matplotlib.pyplot as plt

ks = range(2, 8)
max_vals = [sum([9 * math.pow(10, i) for i in range(k)]) for k in ks]
pows = [sum([math.pow(9, 5) for i in range(k)]) for k in ks]

plt.plot(ks, pows, label="sum of fifth powers of digits")
plt.plot(ks, max_vals, label="number")
plt.tight_layout()
plt.legend()
plt.show()
