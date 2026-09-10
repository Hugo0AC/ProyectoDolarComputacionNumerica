def valor_anual(datos_anuales):
    lista_valores = []
    for dato in datos_anuales:
        lista_valores.append(float(dato[-1]))
    return lista_valores

def var_enero_diciembre(diciembre, enero):
    variacion = diciembre - enero
    return variacion

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

