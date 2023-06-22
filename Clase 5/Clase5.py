class Complejo:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    def __str__(self):
        return('{} + {}i'.format(self.r, self.i))

    def multiplicacionEscalar(self, escalar: int):
        self.r=self.r*escalar
        self.i=self.i*escalar

    def modulo(self):
        z = (self.r**2+self.i**2)**(1/2)
        return z

    def conjugado(self):
        self.r=self.r*(-1)
        self.i=self.i*(-1)