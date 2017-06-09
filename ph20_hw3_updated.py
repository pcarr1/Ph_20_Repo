# Philip Carr
# Friday Section
# Ph 20 Homework 3
# 5/2/2017

import numpy as np
import matplotlib.pyplot as plt

figure_number = 1

# Part 1
# 1.
def plotPositionAndVelocity(xList, vList, tList, numericalType):
    global figure_number
    plt.plot(tList, xList)
    plt.xlabel('t')
    plt.ylabel('x(t)')
    plt.title('x(t) using ' + numericalType + ' Euler method')
    plt.savefig('plots/figure_' + str(figure_number) + '.png')
    figure_number += 1
    plt.show()
    plt.plot(tList, vList)
    plt.xlabel('t')
    plt.ylabel('v(t)')
    plt.title('v(t) using ' + numericalType + ' Euler method')
    plt.savefig('plots/figure_' + str(figure_number) + '.png')
    figure_number += 1
    plt.show()

def explicitEuler(h):
    N = 500
    tList = np.zeros(N + 1)
    xList = np.zeros(N + 1)
    vList = np.zeros(N + 1)
    xList[0] = 1
    vList[0] = 0
    for i in range(1, N + 1):
        tList[i] = tList[i-1] + h
        xList[i] = xList[i-1] + h * vList[i-1]
        vList[i] = vList[i-1] - h * xList[i-1]
    return xList, vList, tList

#2.
def plotEulerError(xErrorList, vErrorList, tList, numericalType):
    global figure_number
    plt.plot(tList, xErrorList)
    plt.xlabel('t')
    plt.ylabel('x(t) error')
    plt.title('Error in x(t) using ' + numericalType + ' Euler method')
    plt.savefig('plots/figure_' + str(figure_number) + '.png')
    figure_number += 1
    plt.show()
    plt.plot(tList, vErrorList)
    plt.xlabel('t')
    plt.ylabel('v(t) error')
    plt.title('Error in v(t) using ' + numericalType + ' Euler method')
    plt.savefig('plots/figure_' + str(figure_number) + '.png')
    figure_number += 1
    plt.show()

def getEulerError(xList, vList, tList):
    xAnalyticList = tList[:]
    vAnalyticList = tList[:]
    xAnalyticList = np.cos(xAnalyticList)
    vAnalyticList = -np.sin(vAnalyticList)
    xErrorList = xAnalyticList - xList
    vErrorList = vAnalyticList - vList
    return xErrorList, vErrorList

# 3.
def plotTruncationError(numericalType):
    global figure_number
    h = 0.1
    i = 1
    max_xErrorList = np.zeros(5)
    max_vErrorList = np.zeros(5)
    hList = np.zeros(5)
    count = 0
    while i <= 16:
        if numericalType == 'explicit':
            xList, vList, tList = explicitEuler(h)
        elif numericalType == 'implicit':
            xList, vList, tList = implicitEuler(h)
        else:
            raise ValueError('numericalType needed!')
        xErrorList, vErrorList = getEulerError(xList, vList, tList)
        hList[count] = h
        max_xErrorList[count] = max(xErrorList)
        max_vErrorList[count] = max(vErrorList)
        i *= 2
        h /= 2
        count += 1
    plt.plot(hList, max_xErrorList)
    plt.xlabel('h')
    plt.ylabel('x(t) max error')
    plt.title('Max error in x(t) vs h using ' + numericalType + ' Euler method')
    plt.savefig('plots/figure_' + str(figure_number) + '.png')
    figure_number += 1
    plt.show()
    plt.plot(hList, max_vErrorList)
    plt.xlabel('h')
    plt.ylabel('v(t) max error')
    plt.title('Max error in v(t) vs h using ' + numericalType + ' Euler method')
    plt.savefig('plots/figure_' + str(figure_number) + '.png')
    figure_number += 1
    plt.show()

# 4.
def plotTotalEnergy(xList, vList, tList, numericalType):
    global figure_number
    totalEnergyList = np.power(xList, 2) + np.power(vList, 2)
    plt.plot(tList, totalEnergyList)
    plt.xlabel('t')
    plt.ylabel('E(t)')
    plt.title('Total energy E(t) using ' + numericalType + ' Euler method')
    plt.savefig('plots/figure_' + str(figure_number) + '.png')
    figure_number += 1
    plt.show()

# 5.
def implicitEuler(h):
    N = 500
    tList = np.zeros(N + 1)
    xList = np.zeros(N + 1)
    vList = np.zeros(N + 1)
    xList[0] = 1
    vList[0] = 0
    for i in range(1, N + 1):
        tList[i] = tList[i-1] + h
        xList[i] = (xList[i-1] - h * vList[i-1]) / (1 + np.power(h, 2))
        vList[i] = (vList[i-1] + h * xList[i-1]) / (1 + np.power(h, 2))
    return xList, vList, tList

# Part 2
# 1.
def phaseSpacePlot(xList, vList, numericalType):
    global figure_number
    plt.plot(xList, vList)
    plt.xlabel('x(t)')
    plt.ylabel('v(t)')
    plt.title('v(t) vs x(t) of ' + numericalType + ' Euler method')
    plt.savefig('plots/figure_' + str(figure_number) + '.png')
    figure_number += 1
    plt.show()

# 2.
def phaseSpacePlotAllThreeEulerMethods(allLists):
    global figure_number
    plt.plot(allLists[0], allLists[1], label='explicit Euler method')
    plt.plot(allLists[3], allLists[4], label='implicit Euler method')
    plt.plot(allLists[6], allLists[7], label='symplectic Euler method')
    plt.xlabel('x(t)')
    plt.ylabel('v(t)')
    plt.title('v(t) vs x(t) of explicit, implicit, and symplectic Euler method')
    plt.legend()
    plt.savefig('plots/figure_' + str(figure_number) + '.png')
    figure_number += 1
    plt.show()

def symplecticEuler(h):
    N = 500
    tList = np.zeros(N + 1)
    xList = np.zeros(N + 1)
    vList = np.zeros(N + 1)
    xList[0] = 1
    vList[0] = 0
    for i in range(1, N + 1):
        tList[i] = tList[i-1] + h
        xList[i] = xList[i-1] + h * vList[i-1]
        vList[i] = vList[i-1] - h * xList[i]
    return xList, vList, tList

def main():
    h = 0.1
    xListE, vListE, tListE = explicitEuler(h)
    plotPositionAndVelocity(xListE, vListE, tListE, 'explicit')
    xErrorListE, vErrorListE = getEulerError(xListE, vListE, tListE)
    plotEulerError(xErrorListE, vErrorListE, tListE, 'explicit')
    plotTruncationError('explicit')
    plotTotalEnergy(xListE, vListE, tListE, 'explicit')

    h = 0.1
    xListI, vListI, tListI = implicitEuler(h)
    plotPositionAndVelocity(xListI, vListI, tListI, 'implicit')
    xErrorListI, vErrorListI = getEulerError(xListI, vListI, tListI)
    plotEulerError(xErrorListI, vErrorListI, tListI, 'implicit')
    plotTruncationError('implicit')
    plotTotalEnergy(xListI, vListI, tListI, 'implicit')

    phaseSpacePlot(xListE, vListE, 'explicit')
    phaseSpacePlot(xListI, vListI, 'implicit')
    h = 0.1
    xListS, vListS, tListS = symplecticEuler(h)
    plotPositionAndVelocity(xListS, vListS, tListS, 'symplectic')
    phaseSpacePlot(xListS, vListS, 'symplectic')
    allLists = [xListE, vListE, tListE, xListI, vListI, tListI
                , xListS, vListS, tListS]
    phaseSpacePlotAllThreeEulerMethods(allLists)
    plotTotalEnergy(xListS, vListS, tListS, 'symplectic')

if __name__ == '__main__': main()
