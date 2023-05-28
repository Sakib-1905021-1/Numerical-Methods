import numpy as np
import math
import matplotlib.pyplot as plt


# def plotGraph():
#     xvalues = np.arange(1900, 2010, 10)
#     yvalues = np.array([10.3, 13.5, 13.9, 14.2, 11.6, 10.3, 9.7, 9.6, 14.1, 19.8, 31.1])
#     plt.plot(xvalues, yvalues, marker='o')
#
#     font1 = {'family': 'Algerian', 'color': 'red', 'size': '18'}
#
#     plt.xlabel("x-axis")
#     plt.ylabel("y-axis")
#
#     plt.axhline(y=0, c='#606060')
#     plt.axvline(x=1900, c='#606060')
#     plt.grid()
#     plt.title("Curve Fitting", fontdict=font1)
#     plt.show()
#
#
# if __name__ == '__main__':
#     plotGraph()

import numpy as np


def pivotForwardElimination(mat_a, mat_b, pivotRow, numOfVar):

    largestRow = pivotRow

    # find index of largest abs value of mat_a[pivotRow -> numOfVar][pivotRow]
    for currRow in range(pivotRow, numOfVar):
        if (abs(mat_a[currRow][pivotRow]) > abs(mat_a[largestRow][pivotRow])):
            largestRow = currRow

    # swap pivotRow with largestRow
    mat_a[[pivotRow, largestRow]] = mat_a[[largestRow, pivotRow]]
    mat_b[[pivotRow, largestRow]] = mat_b[[largestRow, pivotRow]]

    return mat_a, mat_b


def BackSubstitution(mat_a, mat_b, mat_res, numOfVar):

    # back substitution loop, we loop for numOfVar time, from back, 0 index so -1
    for variable in range(numOfVar):
        curr_row = numOfVar - 1 - variable

        divider = mat_a[curr_row][curr_row]

        upper_one = mat_b[curr_row][0]
        upper_two = 0

        if (curr_row < numOfVar - 1):
            for moreRow in range(curr_row + 1, numOfVar):
                upper_two += mat_a[curr_row][moreRow] * mat_res[moreRow][0]

        mat_res[curr_row][0] = (upper_one - upper_two) / divider

    return mat_res


def ForwardElimination(mat_a, mat_b, numOfVar, pivot=True, showall=True):
    for row in range(numOfVar - 1):
        # track variable for printing information
        subStep = 0

        if (showall):
            print("Step: ", row + 1)

        if (pivot):
            mat_a, mat_b = pivotForwardElimination(mat_a, mat_b, row, numOfVar)

        for nextRow in range(row + 1, numOfVar):
            subStep += 1

            multipler = mat_a[nextRow][row] / mat_a[row][row]

            currA_row = mat_a[row] * multipler
            currB_row = mat_b[row] * multipler

            mat_a[nextRow] -= currA_row
            mat_b[nextRow] -= currB_row

            if (showall):
                print("Sub Step: ", subStep)
                with np.printoptions(precision=4, suppress=True):
                    print("Co-efficient Matrix")
                    print(mat_a)
                    print("Constant matrix")
                    print(mat_b)
                print("\n")

    return mat_a, mat_b


def GaussianElimination(mat_a, mat_b, pivot=True, showAll=True):

    mat_a = np.array(mat_a, dtype=np.double)
    mat_b = np.array(mat_b, dtype=np.double)

    numOfVar, numOfCol = mat_a.shape
    mat_res = np.zeros((numOfVar, 1))

    mat_a, mat_b = ForwardElimination(mat_a, mat_b, numOfVar, pivot, showAll)

    mat_res = BackSubstitution(mat_a, mat_b, mat_res, numOfVar)

    return mat_res


def inputMatrix(rows, cols):
    mat_res = np.zeros((rows, cols))

    for r in range(rows):
        # for c in range(cols):
        mat_res[r] = np.array((input().split()))

    return mat_res

def function(coefficients, x):
    n = len(coefficients)
    y = 0
    for i in range(n):
        y = y + coefficients[i]*(x**i)
    return y

def plotGraph(X, Y) :
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.axhline(y=0, color='k')
    ax.axvline(x=1895, color='k')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title('y = ax^2 + bx + c')
    plt.scatter(X, Y, label='given', color='red', marker='o')
    plt.grid(True, which='both')
    y1 = np.zeros(len(X))
    coefficients = PolynomialRegression(X, Y, 3)
    for i in range (len(x)):
        y1[i] = function(coefficients, X[i])
        #plt.scatter(x, y1, color='green',marker='o')
    plt.plot(X, y1, label='function', color='green', marker='o')
    plt.legend()
    plt.show()

def PolynomialRegression(Xarr, Yarr, order):
    # model: mth order polynomial
    #  y = a_0 + a_1 * x + a_2 * x^2 + a_3 * x^3 + ... + a_m * x^m
    Xarr = np.array(Xarr)
    Yarr = np.array(Yarr)
    total_points = Xarr.size

    coefficient_mat = np.zeros((order+1, order+1), dtype=np.double)
    constant_mat = np.zeros((order + 1, 1), dtype=np.double)

    # fill up coefficient matrix
    # first row special case:
    for row in range(order+1):
        for col in range(order+1):
            if (row == 0 and col == 0):
                coefficient_mat[0][0] = total_points
            else:
                coefficient_mat[row][col] = np.sum(np.power(Xarr, row + col, dtype=np.double))

    # fill up constant matrix
    for row in range(order+1):
        constant_mat[row][0] = np.sum((Yarr * np.power(Xarr, row)))

    # print(coefficient_mat)
    # print(constant_mat)
    # print(np.sum(np.power(Xarr, 2*order, dtype=np.double)))
    return GaussianElimination(coefficient_mat, constant_mat, pivot=True, showAll=False)


temp = [80, 40, -40, -120, -200, -280, -340]
coeff_thermal_expansion = np.array(
    [6.47, 6.24, 5.72, 5.09, 4.30, 3.33, 2.45]) * 1e-6
result = PolynomialRegression(temp, coeff_thermal_expansion, 2)
print(result)

plt.title("Experimental Datas vs Solved Curve")
plt.xlabel("temp")
plt.ylabel("thermal expansion coefficient")

plt.scatter(np.array(temp), np.array(coeff_thermal_expansion), color="green")
# plt.plot(np.array(time), np.array(radiation), color="green")

plt.plot(np.array(temp), result[0][0] + result[1][0] * np.array(temp)
                        + result[2][0] * np.array(temp) * np.array(temp),
                         color="red")

plt.show()

# x = np.array([1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000])
# y = np.array([10.3, 13.5, 13.9, 14.2, 11.6, 10.3, 9.7, 9.6, 14.1, 19.8, 31.1])
# plotGraph(x, y)
# result = PolynomialRegression(x, y, 3)