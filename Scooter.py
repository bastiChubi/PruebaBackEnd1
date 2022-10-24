from Tecnologia import Tecnologia
from Transporte import Transporte

class Scooter:

    def __init__(self,voltaje:int,precio:float,eficiencia:str,marca:str,aro:float,velocidad:int,peso:float):
        Tecnologia.__init__(voltaje, precio, eficiencia, marca)
        Transporte.__init__()
        self.__aro = aro 
        self.__velocidad = velocidad
        self.__peso = peso 
        self.__voltaje = voltaje 
        self.__precio = precio 
        self.__eficiencia = eficiencia
        self.__marca = marca

    def get_aro(self):
        return self.__aro 
    def get_velocidad(self):
        return self.__velocidad
    def get_peso(self):
        return self.__peso 

    def get_voltaje(self):
        return self.__voltaje
    def get_precio(self):
        return self.__precio 
    def get_eficiencia(self):
        return self.__eficiencia
    def get_marca(self):
        return self.__marca

    def set_voltaje(self,voltaje):
        self.__voltaje = voltaje
    def set_precio(self,precio):
        self.__precio = precio 
    def set_eficiencia(self,eficiencia):
        self.__eficiencia = eficiencia 
    def set_marca(self,marca):
        self.__marca = marca 
    

    def set_aro(self,aro):
        self.__aro = aro 
    def set_velocidad(self,velocidad):
        self.__velocidad = velocidad
    def set_peso(self,peso):
        self.__peso = peso

    def __str__(self):
        return f"{super().__str__()}, Aro: {self.__aro}, Velocidad: {self.__velocidad}, Peso: {self.__peso}"

    def calcularDespachoBaseS(self):
        return super().calcularDespachoBaseS()
        
    