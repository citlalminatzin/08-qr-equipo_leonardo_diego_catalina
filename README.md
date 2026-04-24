[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=23621062)
# Práctica 8

¡Adentrémonos en el increíble mundo del álgebra lineal numérica! OwO

## Integrantes

- Juro por Amogasiddhi que si no me escriben los integrantes de su equipo empezando por apellido y ordenados de forma alfabética, lloro

## Uso e instalación

## Ejercicio 1
Calculemos los eigenvalores de: 
$$A = \begin{pmatrix} 5 & -2 \\ -2 & 8 \end{pmatrix}$$

Calculamos el polinomio característico

$$P_A(\lambda) = \det(A - \lambda I)$$

$$= \det \begin{pmatrix} 5 - \lambda & -2 \\ -2 & 8 - \lambda \end{pmatrix}$$

$$= (5 - \lambda)(8 - \lambda) - 4$$

$$= \lambda^2 - 13\lambda + 36$$

$$= (\lambda - 9)(\lambda - 4)$$

$\therefore$ Los eigenvalores son $\lambda_1 = 9$ y $\lambda_2 = 4$

