import numpy as np
import matplotlib.pyplot as plt


# xvalues = np.array([i for i in range(1, 6)])
# yvalues = np.array([i for i in range(1, 6)])
# yvalues2 = np.array([i**3 for i in range(1, 6)])
#
# plt.plot(xvalues, yvalues, xvalues, yvalues2, marker='o')
# plt.show()

mu = 10
sigma = 5

x = mu + sigma * np.random.randn(10000, 3)
n_bucket = 100
labels = ['red', 'green', 'blue']
plt.hist(x, n_bucket, histtype='bar', color=labels, label=labels)
plt.show()