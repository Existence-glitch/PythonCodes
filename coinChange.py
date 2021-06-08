import sys
aux = [0]*(999999)

#Método iterativo (Input: arreglo de denominaciones, monto a cambiar. Output: solución (cantidad mínima de monedas a usar), arreglo que almacena las monedas ocupadas para el cambio)
def bottomUpChange(denom, monto):
    # Se inicializa la tabla que almacena el minimo numero de monedas para el monto i
    # junto a una tabla auxiliar para almacenar la j denominación usada para el monto i
    # Se define tambien la cota inicial como infinito
    table = [0 for i in range (monto+1)]
    tableaux = [0 for i in range (monto+1)]
    cota = sys.maxsize

    # Caso base (Si el monto entregado es 0)
    table[0] = 0

    # Se inicializan todos los valores de la tabla como infinitos (cota)
    for i in range(1, monto+1):
        table[i] = cota

    # Calcular las minímas monedas requeridas para todos los valores desde 1 a monto
    for i in range(1, monto+1):
        for j in range(len(denom)):
            if (i >= denom[j] and table[i- denom[j]]+1 < table[i]):
                table[i] = table[i- denom[j]]+1
                tableaux[i] = j
    solution = table[monto]

    # Excepción donde el valor encontrado es igual a la cota
    if table[monto] == cota:
        return -1
    
    #Generar arreglo de monedas usadas en la solución
    solution_coins = []
    k = monto
    while k:
        solution_coins.append(denom[tableaux[k]])
        k = k - denom[tableaux[k]]

    return solution, solution_coins

#Método recursivo (Input: arreglo de denominaciones, monto a cambiar. Output: solución (cantidad mínima de monedas a usar), arreglo que almacena las monedas ocupadas para el cambio)
def topDownChange(denom, monto):
    #Solución relajada (cota = infinito)
    solution = sys.maxsize
    #Si hay una moneda que complete el monto pedido (si el monto se encuentra en el arreglo de denominaciones)
    if monto in denom:
        #se retorna 1 (que indica que se ocupara 1 moneda) y el valor de esa moneda como arreglo
        return 1, [monto]

    #Este auxiliar cuando es mayor a 0, significa que el monto en el que estamos no es una denominación.
    #Memoriza la solución para el monto en el que nos encontramos (Memoization)
    elif aux[monto] > 0:
        return aux[monto], []

    else:
        #Arreglo que almacenará las monedas ocupadas para el cambio (para la solución óptima)
        solution_coins = []
        for coin in denom:
            if coin < monto:
                #Recursión
                n_monedas, monedas = topDownChange(denom, monto - coin)
                partial_solution = 1 + n_monedas
                #Si la solución parcial encontrada es mejor que la solución presente, se la reemplaza
                if partial_solution < solution:
                    solution = partial_solution
                    solution_coins = monedas + [coin]
                    aux[monto] = solution
                #Si la solución parcial encontrada no es mejor que la solución presente, no se sigue revisando esta "rama" (Branch and Bound)
                else:
                    break
    return solution, solution_coins

#Función que recibe los arreglos que almacenan las monedas ocupadas para el cambio y retorna el arreglo de cantidad de cada denominación como es pedido en la tarea
def denominator(denom, solution_coins):
    sol = [0 for i in range (len(denom))]
    for i in range(len(solution_coins)):
        if solution_coins[i] in denom:
            ind = denom.index(solution_coins[i])
            sol[ind] = sol[ind]+1
    return sol

def main():
    #Arreglo de denominaciones de moneda hardcodeado
    denominations = [365, 91, 52, 28, 13, 7, 4, 1]
    #Ingrese 'n' cantidades a procesar: 
    n = int(input())

    for i in range(n):
        #Ingrese el monto a obtener: 
        monto = int(input())
        
        #Método iterativo
        # minCoins, denomUsadas = bottomUpChange(denominations, monto)
        # solution = denominator(denominations, denomUsadas)
        # print(solution)
        
        #Método recursivo
        minCoins, denomUsadas = topDownChange(denominations, monto)
        solution = denominator(denominations, denomUsadas)
        print(solution)

main()