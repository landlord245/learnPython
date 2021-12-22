class punto:
    def __init__(self, x, y):
        self.X = x
        self.Y = y
    def mostrarPunto(self):
        print("El puntero es (",self.X,",",self.Y,")")

p1=punto(56,89)
p2=punto(-45,98)
p3=punto(78,-5)
p4=punto(-45,-23)
p1.mostrarPunto()
p2.mostrarPunto()
p3.mostrarPunto()
p4.mostrarPunto()