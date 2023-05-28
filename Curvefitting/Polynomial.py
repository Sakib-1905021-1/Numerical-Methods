import numpy as np
import math
import matplotlib.pyplot as plt
from GaussianElimination import GaussianElimination
# def plotGraph1():
#     xvalues = np.array([80, 40, -40, -120, -200, -280, -340])
#     yvalues = np.array([6.47e-6,6.24e-6, 5.72e-6, 5.09e-6, 4.3e-6, 3.33e-6, 2.45e-6])
#
#     plt.plot(xvalues, yvalues, marker='o')
#
#     font1 = {'family': 'Algerian', 'color': 'red', 'size': '18'}
#
#     plt.xlabel("x-axis")
#     plt.ylabel("y-axis")
#
#     plt.axhline(y=0, c='#606060')
#     plt.axvline(x=0, c='#606060')
#     plt.grid()
#     plt.title("Curve Fitting", fontdict=font1)
#     plt.show()


def plotGraph(X, Y) :
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.axhline(y=0, color='k')
    ax.axvline(x=1895, color='k')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title('y = ax^2 + bx + c')
    plt.scatter(X, Y, label='given', color='red', marker='o')
    # plt.grid(True, which='both')
    # y1 = np.zeros(len(X))
    # coefficients = PolynomialRegression(X, Y, 3)
    # for i in range (len(x)):
    #     y1[i] = function(coefficients, X[i])
    #     #plt.scatter(x, y1, color='green',marker='o')
    # plt.plot(X, y1, label='function', color='green', marker='o')
    # plt.legend()
    plt.show()


def function(coefficients, x):
    n = len(coefficients)
    y = 0
    for i in range(n):
        y = y + coefficients[i]*(x**i)
    return y


def getMatrices(x, y, N):
    n = len(x)
    X = np.zeros((N, N))
    Y = np.zeros((N, 1))
    Xpotential = np.ones(n)
    sum_x = np.zeros(2*N - 1)
    for i in range(2*N-1):
        sum_x[i] = sum(Xpotential)
        if i<N:
            Y[i][0] = sum(Xpotential*y)
        Xpotential = Xpotential*x
    for i in range(N):
        for j in range(N):
            X[i][j] = sum_x[i+j]
    return X,Y


def PolynomialRegression(x, y, degree):
    X, Y = getMatrices(x, y, degree+1)
    coefficients = GaussianElimination(X, Y)
    return coefficients


if __name__ == '__main__':
    # x = np.array([80, 40, -40, -120, -200, -280, -340])
    # y = np.array([6.47e-6,6.24e-6, 5.72e-6, 5.09e-6, 4.3e-6, 3.33e-6, 2.45e-6])
    x = np.array([1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000])
    y = np.array([10.3, 13.5, 13.9, 14.2, 11.6, 10.3, 9.7, 9.6, 14.1, 19.8, 31.1])
    plotGraph(x, y)
    #plotGraph1()
    coefficients = PolynomialRegression(x, y, 3)
    print(coefficients)
    y1 = np.zeros(len(x))
    for i in range(len(x)):
        y1[i] = function(coefficients, x[i])
    print(y1)

