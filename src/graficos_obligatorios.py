import matplotlib.pyplot as plt
import errores as err

def grafico_dolar(anios_completos):
    fecha = []
    monto_mes = []

    for anio in range(4):
        for mes in range(12):
            fecha.append(f"{22 + anio}/{mes + 1}")
            monto_mes.append(float(anios_completos[anio][mes][-1]))

    fig, ax = plt.subplots()

    ax.plot(fecha, monto_mes)
    ax.set_xlabel("Meses")
    ax.set_ylabel("Dolar")
    ax.set_title("Dolar entre 2022-2025 por mes")
    ax.tick_params(axis="x", rotation=90)

    fig.tight_layout()
    fig.savefig(
        "graficos\\Grafico_dolar.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close(fig)

def grafico_variacion(anios_completos):
    fecha = []
    monto_mes = []

    for anio in range(4):
        for mes in range(12):
            fecha.append(f"{22 + anio}/{mes + 1}")
            monto_mes.append(float(anios_completos[anio][mes][-1]))

    variacion = []
    for i in range(1, len(monto_mes)):
        variacion.append(monto_mes[i] - monto_mes[i - 1])

    fig, ax = plt.subplots()

    ax.bar(fecha[1:], variacion)
    ax.set_xlabel("Meses")
    ax.set_ylabel("Variacion")
    ax.set_title("Variacion mes a mes")
    ax.axhline(0)
    ax.tick_params(axis="x", rotation=90)

    fig.tight_layout()
    fig.savefig(
        "graficos\\Grafico_variacion.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close(fig)

def grafico_error_representacion(anios_completos):
    #Error de representacion por mes al ocupar 2 cifras significativas
    fecha = []
    monto_mes = []

    for anio in range(4):
        for mes in range(12):
            fecha.append(f"{22 + anio}/{mes + 1}")
            monto_mes.append(float(anios_completos[anio][mes][-1]))

    errores = []
    for monto in monto_mes:
        precio = err.Dinero(monto)
        errores.append(precio.error_verdadero(precio.two_cs()))

    fig, ax = plt.subplots()

    ax.bar(fecha, errores)
    ax.set_xlabel("Meses")
    ax.set_ylabel("Errores")
    ax.set_title("Representacion mensual de error")
    ax.axhline(0)
    ax.tick_params(axis="x", rotation=90)

    fig.tight_layout()
    fig.savefig(
        "graficos\\Grafico_error_representacion.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close(fig)

def grafico_rentabilidad_minimo(anios_completos):
    #Rentabilidad de comprar en el minimo y vender en cada mes posterior
    fecha = []
    monto_mes = []
    for anio in range(4):
        for mes in range(12):
            fecha.append(f"{22 + anio}/{mes + 1}")
            monto_mes.append(float(anios_completos[anio][mes][-1]))

    monto_minimo = min(monto_mes)
    posicion = monto_mes.index(monto_minimo)

    p_minimo = err.Dinero(monto_minimo)
    minimo_trunc = p_minimo.two_cs()
    error_minimo = p_minimo.error_verdadero(minimo_trunc)

    rentabilidad = []
    errores_propagados = []
    for i in range(posicion + 1, len(monto_mes)):
        p_venta = err.Dinero(monto_mes[i])
        venta_trunc = p_venta.two_cs()
        error_venta = p_venta.error_verdadero(venta_trunc)

        r = ((((monto_mes[i]) - monto_minimo) / monto_minimo) * 100)
        error_propagado = abs(r) * ((error_venta / abs(venta_trunc)) + (error_minimo / abs(minimo_trunc)))

        rentabilidad.append(r)
        errores_propagados.append(error_propagado)

    fig, ax = plt.subplots()

    ax.errorbar(
        fecha[posicion + 1:],
        rentabilidad,
        yerr=errores_propagados,
        capsize=4
    )

    ax.set_xlabel("Meses")
    ax.set_ylabel("Rentabilidad")
    ax.set_title("Rentabilidad de comprar en el minimo")
    ax.tick_params(axis="x", rotation=90)

    fig.tight_layout()
    fig.savefig(
        "graficos\\Grafico_rentabilida_minima.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close(fig)

def grafico_deriva(anios_completos):
    monto = 1_000_000
    error = []
    for i in range(4):
        for j in range(12):
            precio = float(anios_completos[i][j][-1])
            usd = err.clp_a_usd(monto, precio)
            clp = err.usd_a_clp(usd, precio)
            error.append(clp- monto)
    meses = range(1, 49)

    fig, ax = plt.subplots()

    ax.plot(meses, error, marker="o")
    ax.set_xlabel("Mes")
    ax.set_ylabel("Error")
    ax.set_title("Error de la ida y vuelta")

    fig.tight_layout()
    fig.savefig(
        "graficos\\Grafico_deriva.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close(fig)