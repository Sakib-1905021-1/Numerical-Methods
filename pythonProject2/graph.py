import numpy as np
import matplotlib.pyplot as plt

hori = np.arange(-0.02, 0.12, .001)
vert = np.arange(-0.02, 0.12, .001)
xLine = np.arange(0.0, 0.12, .001)

# for _, i in enumerate(hori):
#     for _, j in enumerate(vert):
#         print(i, j)

xvalues = np.array([i for _, i in enumerate(hori)])
yvalues = np.array([i ** 3 - 0.165 * i * i + 3.993e-4 for _, i in enumerate(vert)])
xvalues1 = np.array([i for _, i in enumerate(xLine)])

font1 = {'family' : 'Algerian', 'color' : 'red', 'size' : '18'}

plt.xlabel("x")
plt.ylabel("y")

plt.plot(xvalues, yvalues)
plt.axhline(y=0, c='#606060')
plt.axvline(x=0, c='#606060')

plt.grid()
plt.title("Bisection Method", fontdict=font1)
plt.show()
