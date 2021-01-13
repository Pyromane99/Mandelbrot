import numpy as np
import matplotlib.pyplot as plt
import datetime

MAX_ITER = 50
POINT = 600


def Sequence(C):
    iteration = 0
    for i in range(1, MAX_ITER + 1):
        iteration = (iteration ** 2) + C
        if abs(iteration) > 2:
            return i

    return 0


def MandelbrotPlot(xStart, xFinish, yStart, yFinish):
    startTime = datetime.datetime.now()

    X = np.linspace(xStart, xFinish, int(POINT * (3 / 2)))
    Y = np.linspace(yStart, yFinish, POINT)

    Z = []
    for y in range(len(Y)):
        tab = []
        for x in range(len(X)):
            tab.append(Sequence(complex(X[x], Y[y])))
        Z.append(tab)

    c = plt.pcolormesh(X, Y, Z)

    endTime = datetime.datetime.now()
    timeDiff = (endTime - startTime)
    executionTime = timeDiff.total_seconds()
    print("Execution Time : " + str(executionTime) + " seconds")

    plt.colorbar(c)
    plt.show()


MAX_ITER = int(input("Nombre maximum d'itérations (50 par défaut) : "))
POINT = int(input("Nombre de points par axe (600 par défaut) : "))
MandelbrotPlot(-2, 1, -1, 1)
