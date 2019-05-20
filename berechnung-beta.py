import numpy as np
from uncertainties import ufloat
from uncertainties.umath import *

a1 = ufloat(-10.9626, 1.0373)
b1 = ufloat(6.04797, 0.482)

a2 = ufloat(-0.5764, 0.8249)
b2 = ufloat(-1.4674, 0.8882)

r = (b2 - b1)/(a1 - a2)

print(r)

e = 1.92 * sqrt(r**2 + 0.22 * r)

print(e)

print(0.13 / 0.72)
print(0.26 / 1.59)