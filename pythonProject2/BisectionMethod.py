from math import fabs

lbound1 = 0
ubound1 = 0

def bisectionMethod(lbound, ubound, arae, maxiteration):
    error = 50
    root = -1
    cnt = 0
    lbound1 = lbound
    ubound1 = ubound
    xL1 = (lbound1**3) - 0.165 * lbound1 * lbound1 + 3.993e-4
    xU1 = (ubound1**3) - 0.165 * ubound1 * ubound1 + 3.993e-4
    if xL1 * xU1 > 0:
        print("There exists no solution in this range")
    elif xL1 * xU1 == 0:
        if xL1 == 0:
            root = lbound1
            # print("Solution is : ")
            # print(lbound1)
        else:
            root = ubound1
            # print("Solution is : ")
            # print(ubound1)
    else:
        while error > arae:
            if error <= arae:
                break
            uvalue = (lbound1 + ubound1) / 2
            if cnt >= 1:
                error = fabs((uvalue - track)/uvalue)
                print(error)
            track = uvalue
            root = track
            xL = (lbound1**3) - 0.165 * lbound1 * lbound1 + 3.993e-4
            xM = (uvalue**3) - 0.165 * uvalue * uvalue + 3.993e-4
            xU = (ubound1**3) - 0.165 * ubound1 * ubound1 + 3.993e-4
            if xL * xM < 0:
                ubound1 = uvalue
            elif xM * xU < 0:
                lbound1 = uvalue
            elif xL * xM == 0 or xM * xU == 0:
                root = uvalue
            cnt += 1

    return root



print("Root of the equation is : ",bisectionMethod(0, 0.11, .0005, 50))









