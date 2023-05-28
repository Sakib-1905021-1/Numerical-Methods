import numpy as np
import math
import matplotlib.pyplot as plt


stocknum = []
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
            y[i] = y[i]/(x[i] - x[j]) #calculating v[0] = v0/(t0-t1)(t0-t2)(t0-t3)....
    return y


def findValue(value, x, y, n):
    sum = 0
    for i in range(n):
        sum = sum + findProducts(i, x, value, n) * y[i] #calculating v0*(t-t1)(t-t2)/(t0-t1)(t0-t2)+.....
    return sum


def readFromfile():
    myfile = open("stock.txt", "r")
    next(myfile)
    for line in myfile:
        stocknum.append([float(x) for x in line.split()])
    print(stocknum)
    myfile.close()


def Interpolation(srtarr, x, y, list, num, val):
    for i in range(num):
        x.append(srtarr[i])
    x = sorted(x)
    #print(x)
    for i in range(num):
        for j in range(len(list)):
            if(list[j][0] == x[i]):
                y.append(list[j][1])
                break
    y = calculateTable(x, y, num)
    #print(y)
    result = findValue(val, x, y, num)
    return result

def plotGraph(xx, yy, n, x, y):
    xvalues = np.arange(0, 200, 5)
    yvalues = findValue(xvalues, xx, yy, n)

    #plt.ylim([lower, upper])
    plt.plot(xvalues, yvalues, marker='o')
    plt.annotate("Interpolated Point", (x, y))

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
    readFromfile()
    X = int(input("Enter a day to know closing index :"))
    length = len(stocknum)
    copyarr = {}
    for i in range(length):
        copyarr[stocknum[i][0]] = abs(stocknum[i][0] - X)
    sortarr = sorted(copyarr, key=copyarr.get)

    n = 4
    x = []
    y = []
    cubic = Interpolation(sortarr, x, y, stocknum, n, X)
    print("Closing index of stock of day X : ", cubic)

    n = n - 1
    x = []
    y = []
    quadratic = Interpolation(sortarr, x, y, stocknum, n, X)

    error = math.fabs((cubic - quadratic)/cubic)*100
    print("Absolute relative approximate error :", error)


    #ploting graph
    n1 = len(stocknum)
    xaxis = [0]*n1
    yaxis = [0]*n1
    for i in range(n1):
        xaxis[i] = stocknum[i][0]
        yaxis[i] = stocknum[i][1]
    calculateTable(xaxis, yaxis, n1)
    plotGraph(xaxis, yaxis, n1, X, cubic)