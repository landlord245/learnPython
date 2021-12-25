class libro():
    def __init__(self, nombreLibro, categoriaLibro):
        self.libro = nombreLibro
        self.categoria = categoriaLibro
        self.letra = nombreLibro[0]

    def dimeLibro(self):
        return print('Libro:', self.libro,'\nCategoria:',self.categoria,'\nInicial:',self.letra,'\n')
        


lotr = libro('Senor de los Anillos', 'Fantasia')
hp = libro('Harry Poter', 'Fantasia')

# lotr.dimeLibro()
