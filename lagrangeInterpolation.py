import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
from numpy import pi

def f(x):
    #f(x) = sin(x)
    return np.sin(x)

def main():
    #1)
    #Lagrange interpolation for f(x) with 9 equidistant points between [0,pi]
    x = np.linspace(0, pi, 9)
    y = f(x)
    polynomial = lagrange(x, y)

    #Evaluating polynomial in 1000 points between [0,pi]
    x2 = np.linspace(0, pi, 1000)
    g = polynomial(x2)

    #Plotting Lagrange interpolation evaluated in 1000 points between [0,pi]
    plt.plot(x2, g)
    plt.xlabel("Lagrange interpolation")
    plt.savefig('lagrange_interpolation.png', format='png')
    plt.show()

    #Evaluating sine in 1000 points between [0,pi]
    y2 = f(x2)

    #Plotting interpolation vs sine evaluated in 1000 points between [0,pi]
    plt.plot(x2, g, x2, y2)
    plt.xlabel("Lagrange interpolation vs original function")
    plt.savefig('interpolation_vs_sine_comparison.png', format='png')
    plt.show()

    #Calculating lagrange interpolation error by |f(x) - g(x)|
    error = abs(y2 - g)

    #Plotting error of Lagrange interpolation
    plt.plot(x2, error)
    plt.xlabel("Lagrange interpolation error")
    plt.savefig('lagrange_interpolation_error.png', format='png')
    plt.show()

main()