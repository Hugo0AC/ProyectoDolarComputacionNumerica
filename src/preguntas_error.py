from anualidades import valor_anual, var_enero_diciembre, meses
import errores as err

def pregunta_a1(valores_anuales):
    #Error de representacion mes a mes
    dinero = valor_anual(valores_anuales)
    objeto_dinero = err.casteo_dinero(dinero)
    valores_truncados = []
    error_absoluto = []
    error_relativo = []

    for obj in objeto_dinero:
        truncado = obj.two_cs()
        valores_truncados.append(truncado)

    for i in range(len(objeto_dinero)):
        error_absoluto.append(objeto_dinero[i].error_verdadero(valores_truncados[i]))
        error_relativo.append(objeto_dinero[i].error_Vrelativo(valores_truncados[i]))

    mes_con_mas_Erelativo = meses[error_relativo.index(max(error_relativo))]
    return error_absoluto, error_relativo, mes_con_mas_Erelativo
    #print(f"Errores relativos: {error_relativo}")
    #print(f"Mes con mayor error relativo: {max(error_relativo)} - ({meses[error_relativo.index(max(error_relativo))]})")


def pregunta_a2(valores_anuales, mes_compra, mes_venta):
    #Evaluacion entre dos puntos (una compra-venta)
    dinero_meses = err.casteo_dinero(valor_anual(valores_anuales))
    truncado_meses = [dinero_meses[i].two_cs() for i in range(len(dinero_meses))]
    monto = 1_000_000

    dolares_comprados = err.clp_a_usd(monto, truncado_meses[mes_compra])
    ganancia = err.usd_a_clp(dolares_comprados, truncado_meses[mes_venta]) - monto

    ER_compra = abs((dinero_meses[mes_compra].valor - truncado_meses[mes_compra]) / dinero_meses[mes_compra].valor)
    ER_venta = abs((dinero_meses[mes_venta].valor - truncado_meses[mes_venta]) / dinero_meses[mes_venta].valor)

    error_relativo_total = ER_compra + ER_venta
    EA_ganancia = abs(ganancia) * error_relativo_total

    error_porcentual = error_relativo_total * 100

    return ganancia, EA_ganancia, error_porcentual
    #print(f"{ganancia} +- {EA_ganancia}")
    #print(f"Error porcentual: {(error_relativo_total * 100):.2f}%")


def pregunta_a3():
    #Cancelacion (dos meses casi iguales)
    diciembre22 = err.Dinero(875.66)
    diciembre23 = err.Dinero(874.67)

    d22_trunc = diciembre22.three_cs() 
    d23_trunc = diciembre23.three_cs()

    variacion = d23_trunc - d22_trunc
    error_2022 = diciembre22.error_verdadero(d22_trunc)
    error_2023 = diciembre23.error_verdadero(d23_trunc)

    error_variacion = error_2022 + error_2023
    error_porcentual = (error_variacion / abs(variacion)) * 100

    return variacion, error_variacion, error_porcentual
    #print(f"Delta_P: {variacion} +- {error_variacion}")
    #print(f"{error_porcentual:.2f}%")


def pregunta_a4(a2022, a2023, a2024, a2025):
    #Anualidades (enero a diciembre)
    clp22 = [valor_anual(a2022)[-1], valor_anual(a2022)[0]]
    clp23 = [valor_anual(a2023)[-1], valor_anual(a2023)[0]]
    clp24 = [valor_anual(a2024)[-1], valor_anual(a2024)[0]]
    clp25 = [valor_anual(a2025)[-1], valor_anual(a2025)[0]]
    cant_anios = 4
    valores_anuales = [clp22, clp23, clp24, clp25]
    valores_truncados = []
    error_propagado = []
    variacion = []
    error_relativoPV = []

    for i in range(cant_anios):
        valores_truncados.append([err.Dinero(valores_anuales[i][0]).two_cs(), err.Dinero(valores_anuales[i][1]).two_cs()])

    for i in range(cant_anios):
        enero = err.Dinero(valores_anuales[i][0]).error_verdadero(valores_truncados[i][0])
        diciembre = err.Dinero(valores_anuales[i][1]).error_verdadero(valores_truncados[i][1])
        error_propagado.append(enero + diciembre)

    for i in range(cant_anios):
        variacion.append(var_enero_diciembre(valores_truncados[i][0], valores_truncados[i][1]))

    for i in range(cant_anios):
        error_relativoPV.append((error_propagado[i] / abs(variacion[i])) * 100)

    orden = [3, 2, 0, 1] #[10.649999999999977, 20.824999999999818, 6.157142857142779, 5.750000000000028] [2025, 2024, 2022, 2023]

    retorno_datos = []
    for i in orden:
        retorno_datos.append([2022 + i, variacion[i], error_propagado[i], error_relativoPV[i]])

    return retorno_datos
    #for i in orden:
    #    print(f"{2022 + i}", end = " ")
    #    print(f"Delta_P: {variacion[i]:.2f} +- {error_propagado[i]:.2f} ;", end = " ")
    #    print(f"Error porcentual: {error_relativoPV[i]:.2f}")


def pregunta_a5(anios):
    #Mejor compra y venta
    solo_valores = []

    for i in range(4):
        for j in range(12):
            solo_valores.append(float(anios[i][j][-1]))

    p_maximo = err.Dinero(max(solo_valores))
    p_minimo = err.Dinero(min(solo_valores))
    max_trunc = p_maximo.two_cs()
    min_trunc = p_minimo.two_cs()

    rentabilidad = ((max_trunc - min_trunc) / min_trunc) * 100
    error_rentabilidad = ((p_maximo.error_verdadero(max_trunc) / max_trunc) + (p_minimo.error_verdadero(min_trunc) / min_trunc)) * 100 
    conclusion = (error_rentabilidad / rentabilidad) * 100

    return rentabilidad, error_rentabilidad, conclusion
    #print(rentabilidad, error_rentabilidad, conclusion)