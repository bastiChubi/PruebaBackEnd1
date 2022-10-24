from Tecnologia import Tecnologia

class Tv(Tecnologia):

    def __init__(self, voltaje: int, precio: float, eficiencia: str, marca: str, tamano:float):
        super().__init__(voltaje, precio, eficiencia, marca)
        self.__tamano = tamano

    def get_tamano(self):
        return self.__tamano

    def set_tamano(self,tamano):
        self.__tamano = tamano
    
    def __str__(self):
        return f"{super().__str__()} Tamaño: {self.__tamano}"