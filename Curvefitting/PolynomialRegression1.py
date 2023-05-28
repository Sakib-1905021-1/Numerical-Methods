import numpy as np
import matplotlib.pyplot as plt
import math
import sys


# x = np.loadtxt("input1.txt", dtype=float, usecols=0)
# y = np.loadtxt("input1.txt", dtype=float, usecols=1)

def coefficient(A, B):
    for i in range(len(B)):
        A[i] = A[i] * B[i]
    return A


def matrix_A_form(A, n):
    c = A.copy()

    coeff_matrix = []  # this is our coeeficient 2d table
    temp = [len(A), sum(A)]
    for i in range(n - 2):
        coefficient(c, A)
        temp.append(sum(c))

    coeff_matrix.append(temp)
    for i in range(n - 1):
        t = np.zeros(n)
        for j in range(n - 1):
            t[j] = temp[j + 1]
        t[n - 1] = sum(coefficient(c, A))
        temp = t.copy()
        coeff_matrix.append(list(t))
    return coeff_matrix


def matrix_B_form(A, B, n):
    d = B.copy()
    arr = []
    temp = [sum(B)]
    arr.append(temp)
    for i in range(n - 1):
        t = [sum(coefficient(d, A))]
        arr.append(t)

    return arr


def show(A, B):
    print("================================================================")
    for i in range(len(B)):
        for j in range(len(B)):
            print('%8.4f' % A[i][j], end='\t')
        print('|    %8.4f' % B[i])


def GaussianElimination(A, B, pivot=True, showall=True):
    n = len(B)
    for k in range(n - 1):
        if pivot == True:
            maxi = np.fabs(A[k, k])
            maxidx = k
            for i in range(k + 1, n):
                if (np.fabs(A[i, k])) > maxi:
                    maxi = np.fabs(A[i, k])
                    maxidx = i
            A[[k, maxidx]] = A[[maxidx, k]]
            B[[k, maxidx]] = B[[maxidx, k]]

        if (np.fabs(A[k, k])) < 1.0e-10:
            sys.exit("Division by 0 found")
        for i in range(k + 1, n):
            factor = A[i, k] / A[k, k]
            for j in range(k, n):
                A[i, j] = A[i, j] - (factor * A[k, j])
            B[i] = B[i] - (factor * B[k])
            if showall:
                show(A, B)

    x = np.zeros(n)
    x[n - 1] = B[n - 1] / A[n - 1, n - 1]
    for i in range(n - 2, -1, -1):
        sum = 0
        for j in range(i + 1, n):
            sum += A[i, j] * x[j]

        if np.fabs(A[i, i]) < 1.0e-12:
            sys.exit("Divition by 0 found")
        x[i] = (B[i] - sum) / A[i, i]

    return x


def func(x_value, ans_arr, n):
    variable = 1
    sum = 0
    for i in range(n):
        sum = sum + ans_arr[i] * variable
        variable = variable * x_value
    return sum


def plot_graph(ar_x, ar_y, sol_matrix, n):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.axhline(y=0, color='k')
    ax.axvline(x=1895, color='k')

    ax.spines['bottom'].set_position('zero')
    f = np.zeros(len(ar_y))
    for i in range(len(ar_y)):
        f[i] = func(ar_x[i], sol_matrix, n)

    plt.grid(color='black', linewidth='0.5')
    plt.xlabel('Temperature', fontweight='bold', color='blue')
    plt.ylabel('Thermal Expansion coefficient', fontweight='bold', color='blue')
    plt.title('Graph', fontweight='bold', color='blue')
    plt.scatter(ar_x, ar_y, label="given data", color='g', marker='o')
    plt.plot(ar_x, f, label='calculated data', color='r', marker='o')
    plt.legend()
    # leg = ax.legend(loc ="lower right");
    plt.show()


n = 4
sz = 11
# x = np.loadtxt("input.txt", dtype=float, usecols=0)
# y = np.loadtxt("input.txt", dtype=float, usecols=1)
#
x = np.array([1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000])
y = np.array([10.3, 13.5, 13.9, 14.2, 11.6, 10.3, 9.7, 9.6, 14.1, 19.8, 31.1])
mat_A = np.array(matrix_A_form(x, n))
mat_B = np.array(matrix_B_form(x, y, n))


# mat_A = np.array([1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000])
# mat_B = np.array([10.3, 13.5, 13.9, 14.2, 11.6, 10.3, 9.7, 9.6, 14.1, 19.8, 31.1])
ans = GaussianElimination(mat_A, mat_B, True, False)
print(ans)
plot_graph(x, y, ans, n)