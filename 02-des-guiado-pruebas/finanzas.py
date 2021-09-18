import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class FinanceException(Exception):
    def __init__(self, msg):
        self.msg = msg


def open_data(file):
    try:
        df = pd.read_csv(file, sep='\t', na_values=['(NA)']).fillna(0)

        if len(df.axes[1]) != 12:
            raise FinanceException(
                'Numero de columnas incorrecto, revise el fichero csv')
        cols = df.columns
        for col in cols:
            df[col] = pd.to_numeric(df[col], errors='coerce')
            df = df.replace(np.nan, 0)

        return df

    except FileNotFoundError:
        print('No se ha encontrado el fichero finanzas2020.csv en el directorio.\nCorrige el error y ejecuta el programa de nuevo, gracias')
        exit()

    except FinanceException as e:
        print(e.msg)
        exit()


def print_tabla(dic,text):
    df = pd.DataFrame([[key, dic[key]]
                      for key in dic.keys()], columns=['Mes', text])
    print(df)


def plot_tabla(dic):
    df = pd.DataFrame([[key, dic[key]]
                      for key in dic.keys()], columns=['Mes', 'Ingresos'])

    df.plot(x="Mes", y="Ingresos")
    plt.show()


def calculation(df):
    cols = df.columns
    saldos = {}

    ingresos = {}
    gastos = {}

    for col in cols:
        lineas = len(df.index)
        ingreso = 0
        gasto = 0
        for linea in range(lineas):
            # print(df[col][linea])
            if int(df[col][linea]) > 0:
                ingreso += df[col][linea]
            else:
                gasto += df[col][linea] * -1

        ingresos[col] = ingreso
        gastos[col] = gasto
        saldos[col] = df[col].sum()

    totalGasto = sum(gastos.values())
    mediaGasto = totalGasto / 12
    totalIngreso = sum(ingresos.values())

    return saldos, ingresos, gastos, mediaGasto, totalGasto, totalIngreso


def return_max(dic):
    return max(dic, key=dic.get)


df = open_data('finanzas2020.csv')

saldos, ingresos, gastos, mediaGasto, totalGasto, totalIngreso = calculation(
    df)
print("Teniendo en cuenta la siguiente tabla\n")
print_tabla(gastos,"Total gasto")
print("El mes con mas gastos es", return_max(gastos))
input('Pulsa ENTER para continuar ')

print("Teniendo en cuenta la siguiente tabla\n")
print_tabla(saldos, "Total saldo")
print("El mes con mas ahorro es", return_max(saldos))
input('Pulsa ENTER para continuar ')

print("La media de gastos al año es de", mediaGasto)
print("El total de ingresos al año es de", totalIngreso)
input('Pulsa ENTER para continuar ')

plot_tabla(ingresos)
