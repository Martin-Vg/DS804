# Codifique un algoritmo en python que tome como argumento un valor flotante, obtenga su cuadrado y lo convierta a entero usando la tecnica de composicion

def composicion(g, f): # creamos nuestra funcion de composicion el cual nos regresa una funcion que aplica ambas entradas en un orden especifico
    def h(x):
        return g(f(x))
    return h

def cuadrado(x): # funcion que retorna el cuadrado de un numero
    return x*x

def entero(x): # Funcion que retorna el entero de un numero
    return int(x)

funcionFinal = composicion(entero, cuadrado) # los argumentos son nuestras funciones recordando que primero se realizara f y despues g
print(funcionFinal(3.3))

