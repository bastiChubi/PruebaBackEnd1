from Transporte import Transporte

class Bicicleta(Transporte):

    def __init__(self, aro:float,peso:float,precio:float,marca:str):
        super().__init__()
        self.__aro = aro
        self.__peso = peso 
        self.__precio = precio 
        self.__marca = marca 

    def get_aro(self):
        return self.__aro
    def get_peso(self):
        return self.__peso
    def get_precio(self):
        return self.__precio
    def get_marca(self):
        return self.__marca

    def set_aro(self,aro):
        self.__aro = aro
    def set_peso(self,peso):
        self.__peso = peso
    def set_precio(self,precio):
        self.__precio = precio 
    def set_marca(self,marca):
        self.__marca = marca
    
    def __str__(self):
        return f"Aro: {self.__aro}, Peso: {self.__peso}, Precio: {self.__precio}, Marca: {self.__marca}"
    
    def calcularDespachoBaseB(self):
        return super().calcularDespachoBaseB()