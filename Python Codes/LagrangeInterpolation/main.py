import numpy as np
import math
import matplotlib.pyplot as plt


genenum = []
def findProducts(index, x, value, n):
    pro = 1
    for i in range(n):
        if i == index:
            continue
        pro = pro*(value - x[i])   #for index 0 (t-t1)*(t-t2)*.......
    return pro


def calculateTable(x, y, n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            y[i] = y[i]/(x[i] - x[j])  #calculating v[0] = v0/(t0-t1)(t0-t2)(t0-t3)....


def findValue(value, x, y, n):
    sum = 0
    for i in range(n):
        sum = sum + findProducts(i, x, value, n) * y[i] #calculating v0*(t-t1)(t-t2)/(t0-t1)(t0-t2)+.....
    return sum


#def getNearest(list, val, x, y)

def plotGraph(xx, yy, n, lower, upper):
    xvalues = np.arange(0, 200, 5)
    yvalues = findValue(xvalues, xx, yy, n)

    plt.ylim([lower, upper])
    plt.plot(xvalues, yvalues)

    font1 = {'family': 'Algerian', 'color': 'red', 'size': '18'}

    plt.xlabel("x-axis")
    plt.ylabel("y-axis")

    plt.axhline(y=0, c='#606060')
    plt.axvline(x=0, c='#606060')
    plt.grid()
    plt.title("Lagrange Interpolation", fontdict=font1)
    plt.show()


if __name__ == '__main__':
    #Reading From file
    genenum = []
    myfile = open("gene.txt", "r")
    for line in myfile:
        genenum.append([float(x) for x in line.split()])
    print(genenum)
    myfile.close()
    value = int(input("Enter a number"))
    n = 4
    x = [0] * n
    y = [0] * n
    #idx = getNearest(genenum, value)
    idx = 2
    idx1 = 0
    for i in range(idx-1, idx+3):
        x[idx1] = genenum[i][0]
        y[idx1] = genenum[i][1]
        idx1 = idx1 + 1
    calculateTable(x, y, n)
    Result = findValue(value, x, y, n)
    res1 = 0
    print("The value of gene at given number is: ", Result)
    print(x)

    #error calculation
    error = ((Result - res1)/Result)*100

    #ploting graph
    n1 = len(genenum)
    xaxis = [0]*n1
    yaxis = [0]*n1
    for i in range(n1):
        xaxis[i] = genenum[i][0]
        yaxis[i] = genenum[i][1]
    calculateTable(xaxis, yaxis, n1)
    plotGraph(xaxis, yaxis, n1, -100, 1500)