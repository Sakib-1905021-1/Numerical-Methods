
import numpy as np
import math
import matplotlib.pyplot as plt


def plotGraph(X, Y, a = 0, b = 0) :
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.scatter(X, Y, label='given data', color='red',marker='o')
    plt.grid(True, which='both')
    if a != 0 :
        x = np.arange(0, 31, 5)
        y = function(a,b,x)
        plt.title('y = ae^(bx)')
        plt.scatter(x, y, label='functional', color='green',marker='o')
        plt.plot(x, y, color= 'blue')
    plt.legend()
    plt.show()


def function(a, b, x):
    return a*(np.exp(b*x))


def expToLinear(x, y):
    n = len(x)
    y = np.log(y)
    d = n*sum(x*x)-sum(x)*sum(x)
    b = (n*sum(x*y) - sum(x)*sum(y))/d
    a = (sum(x*x)*sum(y) - sum(x)*sum(x*y))/d

    return np.exp(a), b


if __name__ == '__main__':
    x = np.arange(0, 31, 5)
    y = np.array([1000, 550, 316, 180, 85, 56, 31])
    plotGraph(x, y)
    print("The best fit model is exponential model. According to the graph.")
    print("The model is : y = ae^bx")

    [a, b] = expToLinear(x, y)

    print('a =', a)
    print('b =', b)

    plotGraph(x, y, a, b)

    y1 = function(a, b, 40)
    y1 = round(y1, 2)
    print('Amount of drug after 40 hours : ', y1)




