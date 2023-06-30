##Imprimir el n-esimo elemento de la serie de fibonacci haciendo uso de la recursividad
from functools import cache
from timeit import repeat

def fibonacci(iteraciones):
    if(iteraciones<0):##se evalua que la cantidad de iteraciones sea mayor a 0 para no causar un error
        return "La cantidad de iteraciones debe ser mayor o igual a 0"
    elif(iteraciones<=1):## en la iteracion 0 y 1 los valores son 0 y 1 respectivamente entonces se evita evaluar
        return iteraciones
    else:
        return fibonacci(iteraciones-1) + fibonacci(iteraciones-2)

@ cache
def fibonacci1(iteraciones):
    if(iteraciones<0):##se evalua que la cantidad de iteraciones sea mayor a 0 para no causar un error
        return "La cantidad de iteraciones debe ser mayor o igual a 0"
    elif(iteraciones<=1):## en la iteracion 0 y 1 los valores son 0 y 1 respectivamente entonces se evita evaluar
        return iteraciones
    else:
        return fibonacci(iteraciones-1) + fibonacci(iteraciones-2)


setup_code = "from __main__ import fibonacci"
stmt = "fibonacci(10)"
times = repeat(setup=setup_code, stmt=stmt, repeat=30, number=10) # se repite la funcion 30 veces e imprimimos el tiempo menor de todas las ejecuciones
print(f"Minimum execution time without cache; {min(times)}") # Minimum execution time without cache; 8.040600005188026e-05

setup_code = "from __main__ import fibonacci1"
stmt = "fibonacci1(10)"
times = repeat(setup=setup_code, stmt=stmt, repeat=30, number=10)# se repite la funcion 30 veces e imprimimos el tiempo menor de todas las ejecuciones
print(f"Minimum execution time with cache; {min(times)}") # Minimum execution time with cache; 5.430001692730002e-07