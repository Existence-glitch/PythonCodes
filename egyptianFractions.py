from math import gcd, ceil

def fibonacci(a, b):
    #Se calcula el denominador de la más grande fracción unitaria ("Largest unit fraction")
    luf_den = ceil(b/a)
    #Resta entre la fracción a/b entregada y la más grande fracción unitaria que podemos extraer de ella.
    subtraction = a/b - 1/luf_den
    #Si la resta retorna 0, se detiene la recursión y el proceso termina retornando el último denominador de la más grande fracción unitaria.
    if(subtraction == 0):
        return [str(luf_den)]
    #Si la resta no es 0, calculamos recursivamente hasta que esto se cumpla.
    else:
        #Se actualiza el numerador y denominador para el siguiente cálculo
        a = int(a * luf_den - b)
        b = int(b * luf_den)
        #Se calcula el máximo comun divisor entre ellos
        g = gcd(b, a)
        #Se retorna el denominador de la más grande fracción unitaria y se llama a la función recursivamente.
        return [str(luf_den)] + fibonacci(int(a/g), int(b/g))

def main():
    #El programa lee n, para saber cuantas fracciones se insertarán.
    n = int(input())
    for i in range(n):
        #Se lee el numerador y denominador de cada fracción insertada
        numerador, denominador = input().split()
        a = int(numerador)
        b = int(denominador)
        #Se asegura que la fraccion insertada no sea unitaria o con numerador > 1
        if (a > 1):
            #Se asegura que la fraccion insertada no sea impropia, es decir mayor a 1
            if (a < b):
                denominators = ", ".join(fibonacci(a, b))
                print(f"{a}/{b}:", denominators)
            else:
                print("La fracción insertada no es propia")
        
        else:
            print("El numerador insertado es inválido")

main()