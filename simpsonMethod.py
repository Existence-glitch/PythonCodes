import numpy as np
from numpy import log

#Se define la función a integrar
def f(x):
    return 1 / log(x)

#Implementación del método de Simpson
#Parámetros: 
#f es la función a integrar 
#a el límite inferior de la integral
#b el límite superior de la integral
#n el número de intervalos
def simpson (f, a, b ,n):
    h = (b - a) / n
    g = f(a) + f(b)
    #Suma de áreas
    for i in range (1, n // 2):
        g = g + 2 * f(a + 2 * i * h)
    for i in range (0, n // 2):
        g = g + 4 * f(a + (2 * i + 1) * h)   
    return h * g / 3

def main():
    li = simpson(f, 2, 3 ,16)
    print("Li(3): ", li)

main()
