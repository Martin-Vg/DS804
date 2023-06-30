''' Implemente una de las siguientes tres estructuras de datos en python (Pilas, colas árboles) con lassiguientes funciones básicas:
    • agregar
    • eliminar
    • buscar'''

pila = [] # Pila a la cual le aplicaremos los metodos
# la pila actua un elemento FIFO por lo que tenemos que apilar los elementos al final y sacar el ultimo

def agregar(x): # funcion agregar que coloca el elemento al final de la pila
    pila.append(x)

def eliminar():# funcion que elimina el ultimo elemento de la pila
    pila.pop()

def buscar(x):# funcion que busca un elemento dentro de la pila
    try:
        return pila.index(x)
    except:
        return None

for i in range(5):
    agregar(i)

print(pila)

eliminar()

print(pila)

print(buscar(2))
print(buscar(7))