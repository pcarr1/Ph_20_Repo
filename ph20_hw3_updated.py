# Philip Carr
# Friday Section
# Ph 20 Homework 3
# 5/2/2017

import numpy as np
import matplotlib.pyplot as plt
import sys

figure_number = 1

# Part 1
# 1.
def plotPositionAndVelocity(xList, vList, tList, numericalType):
    global figure_number
    if figure_number in [1, 8]:
        plt.plot(tList, xList)
        plt.xlabel('t')
        plt.ylabel('x(t)')
        plt.title('x(t) using ' + numericalType + ' Euler method')
        plt.savefig('plots/figure_' + str(figure_number) + '.png')
        plt.plot(tList, vList)
    elif figure_number in [2, 9]:
        plt.xlabel('t')
        plt.ylabel('v(t)')
        plt.title('v(t) using ' + numericalType + ' Euler method')
        plt.savefig('plots/figure_' + str(figure_number) + '.png')

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
    if figure_number in [3, 10]:
        plt.plot(tList, xErrorList)
        plt.xlabel('t')
        plt.ylabel('x(t) error')
        plt.title('Error in x(t) using ' + numericalType + ' Euler method')
        plt.savefig('plots/figure_' + str(figure_number) + '.png')
    elif figure_number in [4, 11]:
        plt.plot(tList, vErrorList)
        plt.xlabel('t')
        plt.ylabel('v(t) error')
        plt.title('Error in v(t) using ' + numericalType + ' Euler method')
        plt.savefig('plots/figure_' + str(figure_number) + '.png')

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
    if figure_number in [5, 12]:
        plt.plot(hList, max_xErrorList)
        plt.xlabel('h')
        plt.ylabel('x(t) max error')
        plt.title('Max error in x(t) vs h using ' + numericalType + ' Euler method')
        plt.savefig('plots/figure_' + str(figure_number) + '.png')
    if figure_number in [6, 13]:
        plt.plot(hList, max_vErrorList)
        plt.xlabel('h')
        plt.ylabel('v(t) max error')
        plt.title('Max error in v(t) vs h using ' + numericalType + ' Euler method')
        plt.savefig('plots/figure_' + str(figure_number) + '.png')

# 4.
def plotTotalEnergy(xList, vList, tList, numericalType):
    global figure_number
    totalEnergyList = np.power(xList, 2) + np.power(vList, 2)
    plt.plot(tList, totalEnergyList)
    plt.xlabel('t')
    plt.ylabel('E(t)')
    plt.title('Total energy E(t) using ' + numericalType + ' Euler method')
    plt.savefig('plots/figure_' + str(figure_number) + '.png')

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
    global figure_number
    figure_number = int(sys.argv[1][sys.argv[1].index('_')+1:-4])
    h = 0.1
    xListE, vListE, tListE = explicitEuler(h)
    xListI, vListI, tListI = implicitEuler(h)
    xListS, vListS, tListS = symplecticEuler(h)
    xErrorListE, vErrorListE = getEulerError(xListE, vListE, tListE)
    xErrorListI, vErrorListI = getEulerError(xListI, vListI, tListI)
    if figure_number in [1, 2]:
        plotPositionAndVelocity(xListE, vListE, tListE, 'explicit')
    elif figure_number in [3, 4]:
        plotEulerError(xErrorListE, vErrorListE, tListE, 'explicit')
    elif figure_number in [5, 6]:
        plotTruncationError('explicit')
    elif figure_number in [7]:
        plotTotalEnergy(xListE, vListE, tListE, 'explicit')
    elif figure_number in [8, 9]:
        plotPositionAndVelocity(xListI, vListI, tListI, 'implicit')
    elif figure_number in [10, 11]:
        plotEulerError(xErrorListI, vErrorListI, tListI, 'implicit')
    elif figure_number in [12, 13]:
        plotTruncationError('implicit')
    elif figure_number in [14]:
        plotTotalEnergy(xListI, vListI, tListI, 'implicit')
    elif figure_number in [15]:
        phaseSpacePlot(xListE, vListE, 'explicit')
    elif figure_number in [16]:
        phaseSpacePlot(xListI, vListI, 'implicit')
    elif figure_number in [17]:
        phaseSpacePlot(xListS, vListS, 'symplectic')
    elif figure_number in [18]:
        allLists = [xListE, vListE, tListE, xListI, vListI, tListI
                    , xListS, vListS, tListS]
        phaseSpacePlotAllThreeEulerMethods(allLists)
    elif figure_number in [19]:
        plotTotalEnergy(xListS, vListS, tListS, 'symplectic')

if __name__ == '__main__': main()
