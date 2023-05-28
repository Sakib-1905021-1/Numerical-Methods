import numpy as np
import math
import matplotlib.pyplot as plt

def integrand (val):
    return ((6.73*val+6.725e-8+7.26e-4*5e-4)/(3.62e-12*val+3.908e-8*val*5e-4))*(-1)


def integration(n, lowerval, upperval):
    h = (upperval - lowerval)/n
    sum = 0.0
    value = 0.0
    for i in range(1, n):
        value = lowerval + i*h
        sum = sum + integrand(value)
    finalres = ((upperval - lowerval)/(2*n))*(integrand(lowerval) + 2*sum + integrand(upperval))
    return finalres


def simpIntegration(n, lowerval, upperval):
    h = (upperval - lowerval)/(2*n)
    sum = 0.0
    for i in range(1, (2*n)):
        value = lowerval + i * h
        if i%2 != 0:
            sum = sum + 4*integrand(value)
        elif i%2 == 0:
            sum = sum + 2*integrand(value)
    finalres = ((upperval - lowerval)/(3*2*n))*(integrand(lowerval)+sum+integrand(upperval))
    return finalres


def arae(n, lowerval, upperval):
    print("Value of n","\t\t", "Absolute Relative Approxomate Error")
    for i in range(n):
        newValue = integration(i+1, lowerval, upperval)

        if i > 0:
            error = (abs(newValue - oldValue)/newValue)*100
            print(i+1, " \t\t\t\t\t ", error, "%")
        if i == 0:
            print(i+1, " \t\t\t\t\t ", "------")
        oldValue = newValue


def simparae(n, lowerval, upperval):
    print("Value of n","\t\t", "Absolute Relative Approxomate Error")
    for i in range(n):
        newValue = simpIntegration(i+1, lowerval, upperval)

        if i > 0:
            error = (abs(newValue - oldValue)/newValue)*100
            print(i+1, " \t\t\t\t\t ", error, "%")
        if i == 0:
            print(i+1, " \t\t\t\t\t ", "------")
        oldValue = newValue


def graphPlot():
    x = [1.22e-4, 1.20e-4, 1.0e-4, 0.8e-4, 0.6e-4, 0.4e-4, 0.2e-4]
    xvalues = np.array(x)
    y = []
    for i in range(len(x)):
        lowerval = x[0]
        upperval = x[i]
        y.append(simpIntegration(10, lowerval, upperval))
    yvalues = np.array(y)
    plt.plot(xvalues, yvalues, marker='o')
    font1 = {'family': 'Algerian', 'color': 'red', 'size': '18'}

    plt.xlabel("oxygen concentration in moles/cm^3")
    plt.ylabel("time for consumption of oxygen in X10^7 second")

    plt.axhline(y=0, c='#606060')
    plt.axvline(x=0, c='#606060')
    plt.grid()
    plt.title("Integration", fontdict=font1)
    plt.show()


if __name__ == '__main__':
    n = int(input("Enter number of sub intervals : "))
    lowerValue = 1.22e-4
    upperValue = 6.1e-5
    print("Number of sub intervals", "Value of integration")
    for i in range(n):
        result = integration(i+1, lowerValue, upperValue)
        print(i+1, "\t\t\t\t\t\t", result)
    arae(n, lowerValue, upperValue)
    print("\n")
    print("Number of sub intervals", "Value of integration")
    for i in range(n):
        result = simpIntegration(i+1, lowerValue, upperValue)
        print(i+1, "\t\t\t\t\t\t", result)
    simparae(n, lowerValue, upperValue)
    graphPlot()








