
# Práctica 8
En esta práctica exploramos el cálculo numérico de eigenvalores para matrices cuadradas simétricas a través del **método de descomposición QR**. El practica documenta la transición desde la teoría matemática hasta su implementación computacional en tres etapas:

1. **Validación analítica:** Cálculo tradicional de valores propios mediante el polinomio característico para establecer un resultado de referencia.
2. **Implementación base:** Desarrollo del algoritmo QR simple utilizando iteraciones fijas para aproximar la matriz a una forma diagonal.
3. **Optimización algorítmica:** Mejora del método mediante la introducción de un criterio de paro basado en una tolerancia de error ($\varepsilon$), lo que optimiza la eficiencia computacional al detener la ejecución una vez alcanzada la convergencia.

## Integrantes
- Marban Ayala Catalina
- Sánchez Ramírez Diego Alberto 

## Ejercicio 1

Calculemos los eigenvalores de la matriz $A$:

$$
A = \begin{pmatrix} 
5 & -2 \\ 
-2 & 8 
\end{pmatrix}
$$

Calculamos el polinomio característico:

$$
P_A(\lambda) = \det(A - \lambda I)
$$

$$
= \det \begin{pmatrix} 5 - \lambda & -2 \\ -2 & 8 - \lambda \end{pmatrix}
$$

$$
= (5 - \lambda)(8 - \lambda) - 4
$$

$$
= \lambda^2 - 13\lambda + 36
$$

$$
= (\lambda - 9)(\lambda - 4)
$$

$\therefore$ Los eigenvalores son $\lambda_1 = 9$ y $\lambda_2 = 4$.
---

## Ejercicio 2

En el ejercicio 2 creamos una función la cual nos ayuda a encontrar los eigenvalores de una matriz cuadrada. Ocupamos la descomposición QR y la iteramos para que los valores de la diagonal se aproximen cada vez más a los eigenvalores.
#### Algoritmo:
```python
def eigenvals_simple(A:list[list[float]], n:int = 100)->list[float]:
    Ak = A 
    for _ in range(n):
        Q,R = qr(Ak)
        Ak =  matmul(R, Q)
    eigenvalores = [Ak[i][i] for i in range(len(A))]
    return eigenvalores 
```
#### Prueba:

Probando el código con la matriz que se nos dio y a la cual ya le sacamos los valores propios mediante el polinomio característico (ejercicio 1), obtenemos lo siguiente:

```python
# Definimos la matriz 
A = [[5, -2],
     [-2, 8]]

# Llamamos a la función y la probamos con 10 iteraciones 
valores_propios = eigenvals_simple(A, n=10)

# Valores obtenidos:
# --> [8.999998191246117, 4.000001808753882]
```

---

## Ejercicio 3

En este ejercicio implementamos una tolerancia, ya que nuestro código anterior puede seguir iterando con valores muy cercanos al cero que ya no nos aportan nada. Definimos la tolerancia como **`1e-10`** y, una vez que los elementos que no están en la diagonal alcanzan esos valores (prácticamente son ceros), el ciclo se detiene anticipadamente, indicando que nuestra matriz ya solo contiene los eigenvalores en su diagonal.

#### Algoritmo (Resumido):
```python
def eigenvals(A: list[list[float]], n: int = 100, tolerance: float = 1e-10):
    Ak = A 
    dim = len(Ak)
    
    for iteracion in range(n):
        # 1. Calculamos QR y actualizamos Ak
        Q, R = qr(Ak)
        Ak = matmul(R, Q)
        
        # 2. Revisamos si los elementos fuera de la diagonal superan la tolerancia
        # ... (Lógica de revisión iterando sobre la matriz) ...
            
        # 3. Criterio de paro anticipado
        if ha_convergido:
            print(f"Convergencia alcanzada en la iteración: {iteracion + 1}")
            break

    # Extraemos y retornamos solo la diagonal principal
    return [Ak[i][i] for i in range(dim)]
```

#### Prueba
Ahora probando el código con la matriz que se nos dio y a la cual ya le sacamos los valores propios mediante el polinomio característico (ejercicio 1), con un codigo sin tolerancia (ejercicio 2) ahora obtenemos lo siguiente:


```python
# Definimos la matriz 
A = [[5, -2],
     [-2, 8]]

# Llamamos a la función y la probamos con 10 iteraciones 
valores_propios = eigenvals(A)

# Valores obtenidos:
# --> Convergencia alcanzada en la iteración: 32
# --> [9.000000000000005, 4.000000000000003]
```
