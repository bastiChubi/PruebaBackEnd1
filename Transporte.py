class Transporte:

    def __init__(self):
        self.__costoDespachoBase = 4000

    def get_costoDespachoBase(self):
        return self.__costoDespachoBase
    def set_costoDespachoBase(self,costoDespachoBase):
        self.__costoDespachoBase = costoDespachoBase

    def calcularDespachoBaseS(self):
        Totalkg = 300
        kgTotal = self.__peso * Totalkg
        total = self.__costoDespachoBase + kgTotal
        print(f"El costo total del despacho del scooter es de {total}")

    def calcularDespachoB(self):
        Totalkg = 400
        cs = 4000
        kgTotal = self.__peso * Totalkg 
        total =  cs + kgTotal
        #total = self.__costoDespachoBase + kgTotal
        print(f"El costo total del despacho de la bicicleta es de {total}")