class Tecnologia:

    def __init__(self,voltaje:int,precio:float,eficiencia:str,marca:str):
        self.__voltaje = voltaje
        self.__precio = precio 
        self.__eficiencia = eficiencia 
        self.__marca = marca 

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
    
    def __str__(self):
        return f"Marca: {self.__marca}, Voltaje: {self.__voltaje}, Precio: {self.__precio}, Eficiencia: {self.__eficiencia}"

    def calcularDescuento(self):
        if self.__eficiencia == "A" or self.__eficiencia == "B":
            descuento = self.__precio * 0.5
            totald = self.__precio - descuento
            print(f"El descuento del producto es de {descuento} y su total es {totald}")
        elif self.__eficiencia == "C" or self.__eficiencia == "D":
            descuento = self.__precio * 0.3
            totald = self.__precio - descuento
            print(f"El descuento del producto es de {descuento} y su total es {totald}")
        elif self.__eficiencia == "E" or self.__eficiencia == "F":
            descuento = self.__precio * 0.1
            totald = self.__precio - descuento
            print(f"El descuento del producto es de {descuento} y su total es {totald}")
        else:
            print("Eficiencia no valida, nos se aplicara descuento")
