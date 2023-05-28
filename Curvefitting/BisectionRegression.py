import numpy as np
import math
import matplotlib.pyplot as plt


def readFromFile():
    data = []
    x = []
    y = []
    with open('data.txt') as file:
        data = file.readlines()
    for datum in data:
        a, b = map(float, datum.split())
        x.append(a)
        y.append(b)
    return len(x), x, y


def function(a, b, x):
    return a*x+b*np.exp(x)


def f(b, yex, xy, xex, x2, e2x):
    return yex - (xy - b*xex)*xex/x2 - b*e2x


def BisectionMethod(lower, upper, error, yex, xy, xex, x2, e2x):
    iteration = 0
    track = 0
    err = 50
    while err >= error:
        if err < error:
            break
        mid = (lower + upper)/2
        if iteration >= 1:
            err = math.fabs((mid - track)/mid)*100
            if err < error:
                return mid
        track = mid
        iteration = iteration + 1
        if f(lower, yex, xy, xex, x2, e2x)*f(mid, yex, xy, xex, x2, e2x) < 0:
            upper = mid
        else:
            lower = mid

    return mid


def plotGraph(X, Y ,a, b) :
    plt.xlabel('x')
    plt.ylabel('y')
    plt.scatter(X, Y, color='red',marker='o')
    plt.grid(True, which='both')
    x = np.arange(0, 2.01, .1)
    y = function(a,b,x)
    plt.title('y = ax + be^x')
    plt.scatter(x, y, color='grey',marker='o')
    plt.plot(x, y, color= 'blue')

    plt.show()


if __name__ == '__main__':
    n, x, y = readFromFile()
    x = np.array(x)
    y = np.array(y)
    yex = sum(y*np.exp(x))
    xy = sum(x*y)
    xex = sum(x*np.exp(x))
    x2 = sum(x**2)
    e2x = sum(np.exp(2*x))
    b = BisectionMethod(-1, 1, 0.001, yex,xy,xex,x2,e2x)
    a = (xy - b*xex)/x2
    print('a = ', a, 'b = ', b)
    plotGraph(x, y, a, b)



