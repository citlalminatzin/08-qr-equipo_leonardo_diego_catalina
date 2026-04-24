#!/usr/bin/env python
import numpy as np
from qr import qr
from gram_schmidt import matmul

def eigenvals(A:list[list[float]], n:int = 100, tolerance = 1e-10)->list[float]:
    """
    Realiza n iteraciones del algoritmo QR para calcular 
    los eigenvalores de A

    Devuelve la estimación de los eigenvalores
    """
    #Inicializamos Ak como la matiz original A
    Ak = A 
    
    #Hacemos las n iteraciones
    for _ in range(n):
        #Obtenemos Q y R de la matriz actual
        Q,R = qr(Ak)
        #producto invertido de R * Q
        Ak =  matmul(R, Q)
        eigenvalores = np.diag(Ak).tolist()
    return eigenvalores

#Prueba
if __name__=="__main__":
    #matriz del ejercicio 1
    A_prueba = [
        [5.0, -2.0], 
        [-2.0, 8.0]
    ]
    #con 10 iteraciones 
    valores_propios = eigenvals(A_prueba, n=10)
    print(valores_propios)

    

