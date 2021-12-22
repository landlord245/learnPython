class punto:
    def __init__(self, x, y):
        self.X = x
        self.Y = y
    def mostrarPunto(self):
        print("El puntero es (",self.X,",",self.Y,")")

p1=punto(56,89)
p1.mostrarPunto()

p1.X = 7
p1.mostrarPunto