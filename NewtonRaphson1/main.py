
from math import fabs, acos
import numpy as np
import matplotlib.pyplot as plt

initialVal = 0


def function(value):
    return (value**3) - 12*value*value + (15 / acos(-1))


def derivative(value):
    return 3*value*value - 24*value


def NewtonRaphson(initialGuess, arae, maxiteration):
    print("Iteration No" + "\t\t\t\t" + "Absolute Relative Approximate Error")
    error = 50
    root = -1
    initialVal = initialGuess
    track = initialVal
    cnt = 0
    while error > arae:
        if error <= arae:
            break
        root = track - (function(track)/derivative(track))
        error = fabs((root - track)/root)
        cnt += 1
        if cnt < 10:
            print(cnt, "\t\t\t\t\t\t\t", error)
        elif cnt >= 10:
            print(cnt, "\t\t\t\t\t\t\t\t", error)

        track = root
    return root

def graph():
    hori = np.arange(-0.02, 1.2, .01)
    vert = np.arange(-0.02, 1.2, .01)

    # for _, i in enumerate(hori):
    #     for _, j in enumerate(vert):
    #         print(i, j)

    xvalues = np.array([i for _, i in enumerate(hori)])
    yvalues = np.array([i ** 3 - 12 * i * i + 15/acos(-1) for _, i in enumerate(vert)])

    font1 = {'family': 'Algerian', 'color': 'red', 'size': '18'}

    plt.xlabel("x")
    plt.ylabel("y")

    plt.plot(xvalues, yvalues)
    plt.axhline(y=0, c='#606060')
    plt.axvline(x=0, c='#606060')

    plt.grid()
    plt.title("Newton Raphson Method", fontdict=font1)
    plt.show()


print(NewtonRaphson(4, .0005, 50))
graph()

