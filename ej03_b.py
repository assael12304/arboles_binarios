# Ejercicio 3 - Regla de ordenamiento BST
#
# Parte A
# 1. Insertar [8, 3, 10] en orden:
#    - 8 entra primero -> se convierte en raiz
#    - 3 < 8 -> va a la izquierda de 8
#    - 10 > 8 -> va a la derecha de 8
#
# 2. Arbol con raiz 20, insertar 15:
#    15 es menor que 20, por lo tanto va a la IZQUIERDA.
#    Regla: valores menores siempre a la izquierda del nodo actual.
#
# 3. Insertar un duplicado: simplemente se ignora.
#    El BST no almacena valores repetidos.
#
# Parte B - Insertar 6 en el arbol dado:
#    Paso 1: 6 vs 8  -> 6 < 8  -> bajar izquierda
#    Paso 2: 6 vs 3  -> 6 > 3  -> bajar derecha
#    Paso 3: 6 vs 5  -> 6 > 5  -> bajar derecha (None -> insertar aqui)
#
#    Arbol final:
#        8
#       / \
#      3   10
#       \
#        5
#         \
#          6
#
# Parte C
# Arbol A (10 con izq=5, y 5 con der=12):
#    NO es BST valido. El nodo 12 esta en el subarbol izquierdo
#    de 10, pero 12 > 10. Viola la propiedad fundamental del BST.
#
# Arbol B (10 con izq=5, y 5 con izq=12):
#    NO es BST valido. El 12 esta a la izquierda del 5
#    pero 12 > 5 (deberia ir a la derecha). Doble violacion.

print("Ver comentarios para respuestas del ejercicio 3")
