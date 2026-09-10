import pandas as pd

import preguntas_error as pe
import punto_flotante as pf
import graficos_obligatorios as go
import cargar_datos as cd

import pandas as pd

def generar_archivo(anios_completos):
    resultados = []

    for i in range(4):
        resultado = pe.pregunta_a2(anios_completos[i], 0, 11)
        resultados.append(["A2", 2022 + i, "Enero", "Diciembre", resultado[1], resultado[2]])

    resultado = pe.pregunta_a3()
    resultados.append(["A3", "2022-2023", "Diciembre 2022", "Diciembre 2023", resultado[1], resultado[2]])

    resultados_a4 = pe.pregunta_a4(a2022, a2023, a2024, a2025)

    for resultado in resultados_a4:
        resultados.append(["A4", resultado[0], "Enero", "Diciembre", resultado[2], resultado[3]])

    resultado = pe.pregunta_a5(anios_completos)
    resultados.append(["A5", "Global", "Minimo", "Maximo", resultado[1], resultado[2]])

    df = pd.DataFrame(resultados, columns=[
        "Pregunta",
        "Periodo",
        "Inicio",
        "Fin",
        "Error",
        "Error relativo"
    ])

    df.to_csv("ProblemaDolarSII\\data\\resultados.csv", index=False)

if __name__ == "__main__":
    anios = ["2022", "2023", "2024", "2025"]
    direccion = "ProblemaDolarSII\\data\\dolar_observado_sii_2022_2025.csv"
    datos = cd.obtener_archivos(direccion)
    a2022 = cd.obtener_anio(cd.normalizar_datos(datos), "2022")
    a2023 = cd.obtener_anio(cd.normalizar_datos(datos), "2023")
    a2024 = cd.obtener_anio(cd.normalizar_datos(datos), "2024")
    a2025 = cd.obtener_anio(cd.normalizar_datos(datos), "2025")
    anios_completos = [a2022, a2023, a2024, a2025] 

    """#   ---   6.Preguntas del error a contestar   ---   #"""
    #A1.Error de representacion mes a mes
    abs22, error22, mes22 = pe.pregunta_a1(a2022)
    abs23, error23, mes23 = pe.pregunta_a1(a2023)
    abs24, error24, mes24 = pe.pregunta_a1(a2024)
    abs25, error25, mes25 = pe.pregunta_a1(a2025)
    print("    -----    Anio 2022    -----    ")
    print(f"Errores absolutos: {abs22}\nErrores relativos: {error22}\nMes con mayor relativo: {mes22}\n")
    print("    -----    Anio 2023    -----    ")
    print(f"Errores absolutos: {abs23}\nErrores relativos: {error23}\nMes con mayor relativo: {mes23}\n")
    print("    -----    Anio 2024    -----    ")
    print(f"Errores absolutos: {abs24}\nErrores relativos: {error24}\nMes con mayor relativo: {mes24}\n")
    print("    -----    Anio 2025    -----    ")
    print(f"Errores absolutos: {abs25}\nErrores relativos: {error25}\nMes con mayor relativo: {mes25}\n")

    #A2.Evaluacion entre dos puntos (una compra-venta)
    ganancia, EA_ganancia, error_porcentuala2 = pe.pregunta_a2(a2023, 1, 7)
    print(f"Ganancia: {ganancia} +- {EA_ganancia}")
    print(f"Error porcentual: {error_porcentuala2:.2f}")

    #A3.Cancelacion (dos meses iguales)
    variacion, error_variacion, error_porcentuala3 = pe.pregunta_a3()
    print(f"Delta_P: {variacion} +- {error_variacion}")
    print(f"{error_porcentuala3:.2f}%")

    #A4.Anualidad (variacion enero->diciembre)
    retorno_datos = pe.pregunta_a4(a2022, a2023, a2024, a2025)
    for i in range(len(retorno_datos)):
        print(f"{2022 + i}", end = " ")
        print(f"Delta_P: {retorno_datos[1][i]:.2f} +- {retorno_datos[2][i]:.2f} ;", end = " ")
        print(f"Error porcentual: {retorno_datos[3][i]:.2f}")

    #A5.Mejor compra y mejor venta
    rentabilidad, error_rentabilidad, conclusion = pe.pregunta_a5(anios_completos)
    print(f"Rentabilidad: {rentabilidad} - Error de la rentabilidad: {error_rentabilidad} - Conclusion: {conclusion}")


    """#   ---   7.Preguntas del punto flotante   ---   #"""
    #B1.Cifras significativas = mantisa corta
    pf.pregunta_B1()

    #B2.La ida y vuelta que no vuelve
    pf.pregunta_B2(anios_completos)

    #B3.Cancelacion en la maquina
    pf.pregunta_B3()


    """#   ---   8.Graficas obligatorias (numpy + matplotlib)  ---   #"""
    go.grafico_dolar(anios_completos)
    go.grafico_variacion(anios_completos)
    go.grafico_error_representacion(anios_completos)
    go.grafico_rentabilidad_minimo(anios_completos)
    go.grafico_deriva(anios_completos)


    """#   ---   Archivo CSV   ---   #"""
    generar_archivo(anios_completos)