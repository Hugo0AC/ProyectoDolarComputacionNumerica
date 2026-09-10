import numpy as np

def obtener_archivos(direccion):
    datos = np.genfromtxt(direccion, delimiter=',', dtype=str)
    return datos

def normalizar_datos(datos):
    return np.array(datos[1:], dtype=str)

def obtener_anio(datos, anio):
    dolar_clp = []
    for dato in datos:
        if dato[0] == anio:
            dolar_clp.append(dato)     
    return np.array(dolar_clp)
