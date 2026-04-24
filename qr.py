#!/usr/bin/env python

"""
Realiza la factorización QR de una matriz
"""

from gram_schmidt import gm, transpose, matmul

def qr(M:list[list[float]])->tuple[list[list[float]], list[list[float]]]:
    """Realiza la factorización QR de una matriz M"""
    #trasponemos para tener vectores acostados
    columnasM = transpose(M)
    #usamos gramschmit
    columnasQ = gm(columnasM)
    #la volvemos a vectores columna
    Q = transpose(columnasQ)
    #obtenemos R multiplicando Qt con M
    Qt = columnasQ
    R = matmul(Qt, M)
    return Q,R
