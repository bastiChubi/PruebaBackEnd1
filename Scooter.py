from Tecnologia import Tecnologia
from Transporte import Transporte

class Scooter:

    def __init__(self,voltaje:int,precio:float,eficiencia:str,marca:str,aro:float,velocidad:int,peso:float):
        Tecnologia.__init__()
        Transporte.__init__()
        self.__aro = aro 
        self.__velocidad = velocidad
        self.__peso = peso 

    def get_aro(self):
        return self.__aro 
    def get_velocidad(self):
        return self.__velocidad
    def get_peso(self):
        return self.__peso 

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
        
    