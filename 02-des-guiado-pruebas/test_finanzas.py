import pytest
import finanzas
import pandas as pd
import numpy as np


def test_calculation():
    columnas = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    datos = np.array([[50, 100, 200, 300, 150, 400, 350, 25, 120, 200, 100, 125],
                     [-100, -50, -100, -150, -75, -200, -175, -10, -60, -100, -50, -25]])
    dfTest = pd.DataFrame(datos, columns=columnas)

    rSaldos = {'Enero': -50, 'Febrero': 50, 'Marzo': 100, 'Abril': 150, 'Mayo': 75, 'Junio': 200,
               'Julio': 175, 'Agosto': 15, 'Septiembre': 60, 'Octubre': 100, 'Noviembre': 50, 'Diciembre': 100}
    rIngresos = {'Enero': 50, 'Febrero': 100, 'Marzo': 200, 'Abril': 300, 'Mayo': 150, 'Junio': 400,
                 'Julio': 350, 'Agosto': 25, 'Septiembre': 120, 'Octubre': 200, 'Noviembre': 100, 'Diciembre': 125}
    rGastos = {'Enero': 100, 'Febrero': 50, 'Marzo': 100, 'Abril': 150, 'Mayo': 75, 'Junio': 200,
               'Julio': 175, 'Agosto': 10, 'Septiembre': 60, 'Octubre': 100, 'Noviembre': 50, 'Diciembre': 25}
    rMediaGasto = 91.25
    rTotalGasto = 1095
    rTotalIngreso = 2120

    assert (rSaldos, rIngresos, rGastos, rMediaGasto, rTotalGasto,
            rTotalIngreso) == finanzas.calculation(dfTest)


def test_max():
    testDic = {'Enero': 1, 'Febrero': 2, 'Marzo': 3, 'Abril': -4, 'Mayo': 5, 'Junio': -6,
               'Julio': 7, 'Agosto': -8, 'Septiembre': -9, 'Octubre': 3, 'Noviembre': 1, 'Diciembre': -3}
    result = 'Julio'

    assert result == finanzas.return_max(testDic)
