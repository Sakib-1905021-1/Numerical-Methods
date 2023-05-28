import numpy as np
import math
import matplotlib.pyplot as plt


def f(a0, a1, x):
    return a0+a1*x


def LinearRegression(x, y):
    n = len(x)
    denominator = n*sum(x**2) - sum(x)*sum(x)
    a1 = (n*sum(x*y) - sum(x)*sum(y))/denominator
    a0 = (sum(x**2)*sum(y) - sum(x)*sum(x*y))/denominator
    return a0, a1

def plotGraph(X, Y, a0 = 0, a1 = 0, a = 0) :
    plt.xlabel('x')
    plt.ylabel('y')
    plt.scatter(X, Y, color='red',marker='o')
    plt.grid(True, which='both')
    if a != 0 :
        x = X
        y = f(a0, a1, x)
        plt.title('y = mx + c')
        plt.scatter(x, y, color='grey',marker='o')
        plt.plot(x, y, color= 'blue')

    plt.show()


if __name__ == '__main__':
    n = int(input("Enter number of points"))

    x = np.zeros(n)
    y = np.zeros(n)
    for i in range(n):
        x[i], y[i] = map(float, input().split())
    plotGraph(x, y)

    a0, a1 = LinearRegression(x, y)
    plotGraph(x, y, a0, a1, 1)
    print(f(a0, a1, 5))