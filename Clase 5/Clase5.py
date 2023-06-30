class Complejo:
    def __init__(self, realpart, imagpart):# funcion inicial para asignar valores de la parte imaginaria y real
        self.r = realpart
        self.i = imagpart

    def __str__(self):# funcion para imprimir el numero con formato al hacerlo string
        return('{} + {}i'.format(self.r, self.i))

    def multiplicacionEscalar(self, escalar: int): # funcion para multiplicar nuestro numero imaginario por un escalar
        self.r=self.r*escalar
        self.i=self.i*escalar

    def modulo(self):
        z = (self.r**2+self.i**2)**(1/2) # operacion para obtener el modulo de nuestro numero
        return z

    def conjugado(self):# funcion de conjugados
        self.r=self.r*(-1)
        self.i=self.i*(-1)