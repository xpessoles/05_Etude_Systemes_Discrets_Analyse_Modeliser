# -*- coding: utf-8 -*-
"""
@author: Xavier Pessoles
"""
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
from math import pi


xi,xf = 0,12

plt.subplot(2,1,1)
plt.ylabel("Voie $A$")
#plt.xlabel("Temps $s$")
plt.grid(True, which="both", linestyle="dotted")

plt.axis([xi,xf,0,1.2])
plt.subplot(2,1,2)

plt.ylabel("Voie $B$")
plt.xlabel("Temps $s$")
plt.grid(True, which="both", linestyle="dotted")
plt.axis([xi,xf,0,1.2])

plt.show()



