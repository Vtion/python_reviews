import numpy as np
import matplotlib.pyplot as plt

N = 100
x = np.random.rand(N)
y = -x + np.random.rand(N)*0.5
#  s= area , c=color, marker=形状 哦o v * < > 1 2 3 4  s p ...
plt.scatter(x, y, marker="P")
plt.show()
