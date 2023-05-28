import numpy as np
import math
import matplotlib.pyplot as plt

def plotGraph():
    xvalues = np.array([4, 5, 7, 8, 9, 10])
    yvalues = np.array([5800, 5700, 4200, 4100, 3100, 2500])
    plt.plot(xvalues, yvalues, marker='o')

    font1 = {'family': 'Algerian', 'color': 'red', 'size': '18'}

    plt.xlabel("x-axis")
    plt.ylabel("y-axis")

    plt.axhline(y=0, c='#606060')
    plt.axvline(x=0, c='#606060')
    plt.grid()
    plt.title("Curve Fitting", fontdict=font1)
    #plt.legend()
    plt.show()

plotGraph()