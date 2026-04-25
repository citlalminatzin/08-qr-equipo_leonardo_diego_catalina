#!/usr/bin/env python
from qr import qr
from gram_schmidt import matmul

def eigenvals_simple(A:list[list[float]], n:int = 100)->list[float]:
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

    eigenvalores = [Ak[i][i] for i in range(len(A))]

    return eigenvalores

def eigenvals(A: list[list[float]], n: int = 100, tolerance: float = 1e-10):
    """
    Realiza hasta n iteraciones del algoritmo QR para calcular 
    los eigenvalores de A, ocupando una tolerancia
    """
    Ak = A 
    dim = len(Ak)
    
    for iteracion in range(n):
        # Obtenemos Q y R
        Q, R = qr(Ak)
        Ak = matmul(R, Q)
        
        # Verificamos la convergencia 
        ha_convergido = True
        for i in range(dim):
            # j empieza en i + 1 para revisar solo arriba de la diagonal
            for j in range(i + 1, dim): 
                # Si algún valor absoluto es mayor o igual a la tolerancia, no ha convergido
                if abs(Ak[i][j]) >= tolerance:
                    ha_convergido = False
                    break 
            
            if not ha_convergido:
                break 
                
        # Si la bandera sigue siendo True, todos los valores fuera de la diagonal cumplen la condición
        if ha_convergido:
            print(f"Convergencia alcanzada en la iteración: {iteracion + 1}")
            break

    eigenvalores = [Ak[i][i] for i in range(dim)]
    
    return eigenvalores

#Prueba
if __name__=="__main__":
    #matriz del ejercicio 1
    A_prueba = [
        [5.0, -2.0], 
        [-2.0, 8.0]
    ]
    #con 10 iteraciones 
    valores_propios = eigenvals_simple(A_prueba, n=10)
    print(valores_propios)
    valores_propios2 = eigenvals(A_prueba)
    print(valores_propios2)

