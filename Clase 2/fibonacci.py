##Imprimir el n-esimo elemento de la serie de fibonacci haciendo uso de la recursividad

def fibonacci(iteraciones):
    if(iteraciones<0):##se evalua que la cantidad de iteraciones sea mayor a 0 para no causar un error
        return "La cantidad de iteraciones debe ser mayor o igual a 0"
    elif(iteraciones<=1):## en la iteracion 0 y 1 los valores son 0 y 1 respectivamente entonces se evita evaluar
        return iteraciones
    else:
        return fibonacci(iteraciones-1) + fibonacci(iteraciones-2)

print(fibonacci(14))