import numpy as np
import math
import matplotlib.pyplot as plt
def plotGraph():
    xvalues = np.arange(0.01, .22, 0.02)
    yvalues = np.array([1.03, 1.06, 1.38, 2.09, 3.54, 6.41, 12.6, 22.1, 39.05, 65.32, 99.78])
    plt.plot(xvalues, yvalues)

    font1 = {'family': 'Algerian', 'color': 'red', 'size': '18'}

    plt.xlabel("x-axis")
    plt.ylabel("y-axis")

    plt.axhline(y=0, c='#606060')
    plt.axvline(x=0, c='#606060')
    plt.grid()
    plt.title("Newton Interpolation", fontdict=font1)
    plt.show()


if __name__ == '__main__':
    plotGraph()


