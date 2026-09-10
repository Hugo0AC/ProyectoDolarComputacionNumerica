import numpy as np

class Dinero:
    def __init__(self, valor):
        self.valor = valor

    def two_cs(self): #2 Cifras significativas
        two = np.round(self.valor, -1)
        return float(two)

    def three_cs(self): #3 Cifras significativas
        three = np.round(self.valor, 0)
        return float(three)

    def error_verdadero(self, num_trunc):
        error = abs(self.valor - num_trunc)
        return float(error)

    def error_Vrelativo(self, num_trunc):
        error = abs(self.valor - num_trunc) / self.valor
        return float(error)

    def error_VrelativoP(self, num_trunc):
        error = (abs(self.valor - num_trunc) / self.valor) * 100
        return float(error)

def casteo_dinero(valores):
    lista_dinero = []
    for valor in valores:
        lista_dinero.append(Dinero(valor))
    return lista_dinero

def usd_a_clp(usd, clp):
    return usd * clp

def clp_a_usd(clp, usd):
    return clp / usd


