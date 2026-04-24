#!/usr/bin/env python

"""
Calcula la factorización de gram-schmidt
para una matriz de tamaño n
"""
from math import sqrt

def dot(x:list[float], y:list[float])->float:
    """Producto punto entre dos vectores"""
    if len(x)!=len(y):
        raise ValueError("No son del mismo tamaño")
    return sum(xi*yi for xi,yi in zip(x,y))   #multiplicamos cada entrada y luego sumamos todo 


def transpose(M:list[list[float]])->list[tuple[float]]:
    """Devuelve traspuesta de una matriz"""
    Mt = []  
    renglones = len(M)
    #los renglones deben tener la misma cantidad de elementos, ent escogemos el primero para saber cuantas columnas hay
    columnas = len(M[0]) 
    #nuestras columnas ahora van a ser los renglones
    for i in range(columnas):
        renglon = []
        for j in range(renglones):
            renglon.append(M[j][i])
        Mt.append(renglon)
    return Mt

def matmul(A:list[list[float]], B:list[list[float]])->list[list[float]]:
    """Multiplicación de dos matrices"""
    """Multiplicación de dos matrices"""
    #columnas de A y renglones de B
    m = len(A[0])
    n = len(B)
    if m != n: 
        raise ValueError("No se pueden multiplicar las matrices")
        
    AB = []
    for i in range(len(A)):   #fijamos un renglon de A
            renglon = []
            for j in range(len(B[0])):   #fijamos una columna de B
                value = 0
                for k in range(m):  #recorremos los valores del renglon y hacemos la multiplicacion
                    value += A[i][k] * B[k][j]
                renglon.append(value)
            AB.append(renglon)
    return AB

def matvec(A:list[list[float]], v:list[float]) -> list[float]:
    """Multiplicación de matriz por un vector"""
    #dimensiones de la matriz
    renglonesA = len(A)
    columnasA = len(A[0])

    if columnasA != len(v):
        raise ValueError("No se puede hacer la multiplicacion")
    
    mult = []
    for i in range(renglonesA):
        valor = 0
        for k in range(columnasA):
            valor += A[i][k]*v[k]
        mult.append(valor)
    return mult

def norm(x:list[float])->float:
    """Obtiene la norma 2 de un vector"""
    return sqrt(dot(x,x))


def proj(u:list[float], v:list[float])->list[float]:
    """Calcula la proyección de u en v"""
    if norm(v) == 0:
        raise ValueError("No hay proyeccion sobre el vector 0")
        
    escalar = dot(v,u)/dot(v,v)
    return [escalar*vi for vi in v]

def normalize(u:list[float])->list[float]:
    """Normaliza un vector"""
    if norm(u) == 0:
        raise ValueError("No se puede normalizar el vector 0")
    return [(1/norm(u))*ui for ui in u]

def matrix_to_str(matrix: list[list[float]])->str:
    """Convierte una matriz a texto"""
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    # return '\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix])
    return '\n'.join(table)

def gm(vectores:list[list[float]])->list[list[float]]:
    base_ort = []    
    for a in vectores:
        # Copiamos el vector original para ir restándole las proyecciones
        v = list(a) 
        
        for q in base_ort:
            escalar = dot(a, q)
            proyeccion = [escalar*qi for qi in q]
            # Restamos la proyección: v = v - proj
            v = [v[i] - proyeccion[i] for i in range(len(v))]
        # Normalizamos el vector resultante
        n = norm(v)
        q_final = [vi / n for vi in v]
        base_ort.append(q_final)
        
    return base_ort
