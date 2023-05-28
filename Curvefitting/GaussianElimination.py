import numpy as np
import sys


def GaussianElimination(A, B):
    n = len(A)
    a = np.zeros((n, n+1))
    x = np.zeros(n)
    for i in range(n):
        for j in range(n+1):
            if j == n:
                a[i][j] = B[i][0]
            else:
                a[i][j] = A[i][j]
    for i in range(n):
        if a[i][i] == 0.0:
            sys.exit('Divide by zero detected!')
        for j in range(i+1, n):
            ratio = a[j][i] / a[i][i]
            for k in range(n+1):
                a[j][k] = a[j][k] - ratio*a[i][k]

    x[n-1] = a[n-1][n]/a[n-1][n-1]
    for i in range(n-2, -1, -1):
        x[i] = a[i][n]
        for j in range(i+1,n):
            x[i] = x[i] - a[i][j]*x[j]
        x[i] = x[i]/a[i][i]

    return x



if __name__ == '__main__':
    n = int(input())
    A = np.zeros((n, n))
    B = np.zeros((n, 1))
    for i in range(n):
        A[i] = np.array([list(map(float, input().split()))], float)
    #input()
    for i in range(n):
        B[i][0] = float(input())
    x = GaussianElimination(A, B)
    for row in x:
        print(row)
