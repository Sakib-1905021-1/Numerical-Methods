import numpy as np
import math
import matplotlib.pyplot as plt


genenum = []
def findProducts(index, x, value):
    pro = 1
    for i in range(index):
        pro = pro*(value-x[i])
    return pro


def calculateTable(x, y, n):
    for i in range(1,n):
        for j in range(n-i):
            y[j][i] = ((y[j][i-1] - y[j+1][i-1])/(x[j] - x[j+1]))
    return y


def findValue(value,x,y,n):
    sum = y[0][0]
    for i in range(1,n):
        sum = sum+ findProducts(i, x, value)*y[0][i]
    return sum


def readFromfile():
    myfile = open("gene.txt", "r")
    for line in myfile:
        genenum.append([float(x) for x in line.split()])
    print(genenum)
    myfile.close()


def Interpolation(srtarr, x, y, list, num, val):
    for i in range(num):
        x.append(srtarr[i])
    x = sorted(x)
    #print(x)
    for i in range(num):
        for j in range(len(list)):
            if(list[j][0] == x[i]):
                y[i][0] = list[j][1]
                break
    y = calculateTable(x, y, num)
    #print(y)
    result = findValue(val, x, y, num)
    return result



def plotGraph(xx, yy, n, lower, upper):
    xvalues = np.arange(0, 40, 0.05)
    yvalues = findValue(xvalues, xx, yy, n)

    plt.ylim([lower, upper])
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
    #Reading From file
    readFromfile()
    value = int(input("Enter a number"))
    n2 = len(genenum)
    #copyarr = [0] * n2
    temp = []
    for i in range(n2):
        temp.append(genenum[i][0])
    copyarr = {}
    for i in range(n2):
        copyarr[int(temp[i])] = abs(genenum[i][0] - value)
    sortarr = sorted(copyarr, key = copyarr.get)



    n = 4
    x = []
    dimensions = (4, 4)
    y = np.zeros(dimensions)
    cubic = Interpolation(sortarr, x, y, genenum, 4, value)
    print("value for cubic : ", cubic)
    n = 3
    x = []
    dimensions = (3, 3)
    y = np.zeros(dimensions)
    quadratic = Interpolation(sortarr, x, y, genenum, 3, value)
    print("Value for quadratic : ", quadratic)

    error = math.fabs((cubic - quadratic)/cubic)*100
    print("Absolute relative approximate error :", error)



    #ploting graph
    n1 = len(genenum)
    xaxis = [0]*n1
    dimensions1 = (n1, n1)
    yaxis = np.zeros(dimensions1)
    for i in range(n1):
        xaxis[i] = genenum[i][0]
        yaxis[i][0] = genenum[i][1]
    calculateTable(xaxis, yaxis, n1)
    plotGraph(xaxis, yaxis, n1, 0,10)




    #"C:\\Users\\HP\\PycharmProjects\\NewtonInterpolation\\gene.txt"