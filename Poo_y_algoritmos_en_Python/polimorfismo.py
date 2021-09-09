
class Persona:
    def __init__(self,nombre):
        self.nombre = nombre

    def avanza(self):
        print("Estoy caminando")


class Ciclista(Persona):

    def __init__(self,nombre):
        super().__init__(nombre)

    def avanza(self):
        print("Estoy bicicletendo")

def main():
    persona = Persona('David')
    persona.avanza()

    ciclista = Ciclista('Daniela')
    ciclista.avanza()
    
if __name__ == '__main__':
    main()