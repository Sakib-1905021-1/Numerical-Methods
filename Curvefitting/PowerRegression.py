# At first plot the curve using giving data
#y = ax^b
import numpy as np
import math
import matplotlib.pyplot as plt
# def plotGraph():
#     xvalues = np.arange(0.01, .22, 0.02)
#     yvalues = np.array([1.03, 1.06, 1.38, 2.09, 3.54, 6.41, 12.6, 22.1, 39.05, 65.32, 99.78])
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

def plotGraph(X, Y ,a = 0 ,b = 0) :
    plt.xlabel('x')
    plt.ylabel('y')
    plt.scatter(X, Y, color='red',marker='o')
    plt.grid(True, which='both')
    if a != 0 :
        x = np.arange(0, 0.23,0.02)
        y = func(a,b,x)
        plt.title('y = ae^(bx)')
        plt.scatter(x, y, color='grey',marker='o')
        plt.plot(x, y, color= 'blue')

    plt.show()


def func(a, b, x):
    return a*(x**b)


def expToLinear(x, y):
    n = len(x)
    y = np.log(y)
    x = np.log(x)
    d = n*sum(x*x)-sum(x)*sum(x)
    b = (n*sum(x*y) - sum(x)*sum(y))/d
    a = (sum(x*x)*sum(y) - sum(x)*sum(x*y))/d

    return np.exp(a), b;

if __name__ == '__main__':
    #plotGraph()
    x = np.array([0.01, 0.03, 0.05, 0.07, 0.09, 0.11, 0.13, 0.15, 0.17, 0.19, 0.21])
    y = np.array([1.03, 1.06, 1.38, 2.09, 3.54, 6.41, 12.6, 22.1, 39.05, 65.32, 99.78])
    plotGraph(x, y)

    [a, b] = expToLinear(x, y)
    print('a =', a, 'b =', b)

    plotGraph(x, y, a, b)

    y1 = func(a, b, 0.16)
    y1 = round(y1, 2)
    print('y val is = ', y1)
    print("Exponential value is : ", math.exp(1))


