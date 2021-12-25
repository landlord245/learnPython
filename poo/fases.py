class punto:
    def __init__(self, x, y):
        self.X = x
        self.Y = y
    def mostrarPunto(self):
        print("El puntero es (",self.X,",",self.Y,")")

class triangulo:
    def __init__(self, v1, v2, v3):
        self.V1 = v1
        self.V2 = v2
        self.V3 = v3
    def mostrarVertices(self):
        self.V1.mostrarPunto()
        self.V2.mostrarPunto()
        self.V3.mostrarPunto()

v1 = punto(4,5)
v2 = punto(6,5)
v3 = punto(546,678)

triangul = triangulo(v1,v2,v3)
triangul.mostrarVertices()

triangul2 = triangulo(54,87,33)
triangul2.mostrarVertices()