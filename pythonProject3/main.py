from math import fabs

Row = int(input("Enter row or column number: "))
matrix = []
valuematrix = []
getvalue = []
print("Enter entries row wise: ")
for i in range(Row):
    a = []
    for j in range(Row):
        a.append(float(input()))
    matrix.append(a)

for r in range(Row):
    valuematrix.append(float(input()))


def printMatrix():
    for i in range(Row):
        for j in range(Row):
            print(matrix[i][j], end=" ")
        print()
    print()


def printvaluematrix():
    for val in range(Row):
        print(valuematrix[val], end=" ")
    print("\n")


def Operation():
    rowNum = 0
    rowValue = Row
    while rowNum < Row-1:
        if rowNum == Row - 1:
            break
        rowSwitch(rowNum, rowValue)
        UpperTriangularMatrix(rowNum)
        rowNum += 1
        # print("Current Values of Matrix.......")
        # printMatrix()
        # printvaluematrix()


def UpperTriangularMatrix(rowNum):
    idx3 = rowNum
    for row in range(rowNum, Row-1):
        multiplier = matrix[row+1][idx3]/matrix[idx3][idx3]
        valuematrix[row+1] -= (valuematrix[rowNum])*multiplier
        for col in range(rowNum, Row):
            matrix[row+1][col] -= (matrix[rowNum][col])*multiplier
        print("Current values of matrix.....")
        printMatrix()
        printvaluematrix()


def valuerowSwitch(idx1, idx2):
    for index in range(Row):
        temp = valuematrix[idx1]
        valuematrix[idx1] = valuematrix[idx2]
        valuematrix[idx2] = temp


def rowSwitch(colno, row):
    #idx2 = 0
    idx2 = -1
    isfound = False
    arr = []
    arr1 = []
    for rowind in range(colno, row):
        for colind in range(colno, row):
            arr.append(matrix[rowind][colno])
    #print(arr)
    arr1.append(arr[0])
    for indx in range(1, len(arr)-1):
        if arr[indx] != arr[indx+1]:
            arr1.append(arr[indx+1])
    max = abs(arr1[0])
    idx1 = colno
    #print(arr1)
    for idx in range(1, len(arr1)):
        if abs(arr1[idx]) > max:
            max = arr1[idx]
            isfound = True
    if isfound:
        for r in range(row):
            for c in range(row):
                if max == abs(matrix[r][c]):
                    idx2 = r
        for col in range(row):
            temp = matrix[idx1][col]
            matrix[idx1][col] = matrix[idx2][col]
            matrix[idx2][col] = temp
        valuerowSwitch(idx1, idx2)
    #printMatrix()


def getvalues():
    n = Row - 1
    cnt = 0
    subtractor = 0
    column = Row - 1
    for j in range(Row):
        getvalue.append((valuematrix[n] - subtractor)/matrix[n][n])
        subtractor = 0
        cnt += 1
        n -= 1
        if cnt >= 1:
            for col in range(column, Row):
                subtractor += (matrix[n][col]*getvalue[Row - 1 - col])
        column -= 1
    getvalue1 = getvalue[::-1]
    for idx in range(Row):
        print('{:.4f}'.format(getvalue1[idx]))


print("Initial matrix values...")
printMatrix()
printvaluematrix()
Operation()
getvalues()

