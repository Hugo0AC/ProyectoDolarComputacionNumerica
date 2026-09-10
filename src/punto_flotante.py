import numpy as np
import errores as err
import matplotlib.pyplot as plt


def pregunta_B1():
    #Cifras significativas = mantisa corta
    valor = err.Dinero(1000.76)
    dos_cifras = valor.two_cs()
    tres_cifras = valor.three_cs()

    error_tcs = valor.error_verdadero(tres_cifras)
    error_dcs = valor.error_verdadero(dos_cifras)

    print(f"Dos cifras significativas: {dos_cifras} - Error: {error_dcs}")
    print(f"Tres cifras significativas: {tres_cifras} - Error: {error_tcs}")


def pregunta_B2(anios_completos):
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

    ax.scatter(meses, error)
    ax.set_xlabel("Mes")
    ax.set_ylabel("Error")
    ax.set_title("Error de la ida y vuelta")

    fig.tight_layout()
    fig.savefig(
        "graficos\\Grafico_2b.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close(fig)


def pregunta_B3():
    #Cancelacion en la maquina
    primer_val = 874.67
    segundo_val = 875.66

    p32 = np.float32(primer_val)
    s32 = np.float32(segundo_val)

    p64 = np.float64(primer_val)
    s64 = np.float64(segundo_val)

    print(f"Float32: {p32} - {s32} = {p32 - s32}")
    print(f"Float64: {p64} - {s64} = {p64 - s64}")