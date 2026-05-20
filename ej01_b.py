# Ejercicio 1 - Mi primer nodo

class Vertice:
    def __init__(self, valor):
        self.valor      = valor   # informacion que contiene el nodo
        self.izq        = None    # rama izquierda (sin hijo al inicio)
        self.der        = None    # rama derecha  (sin hijo al inicio)

# Parte A - Preguntas conceptuales
# 1. self.izq = None quiere decir que el nodo no tiene
#    conexion hacia la izquierda; ese espacio esta disponible
#    para un futuro hijo.
# 2. Si escribo nodo = Vertice(42), entonces nodo.valor es 42.
# 3. Un arbol donde solo existe la raiz tiene 1 nodo en total.

# Parte B - Esquema del nodo con valor 25:
#
#   [ izq: None | valor: 25 | der: None ]
#         |                       |
#       (vacio)                (vacio)

# Parte C - Tres nodos conectados manualmente
central     = Vertice(10)
central.izq = Vertice(5)
central.der = Vertice(15)

print("central:", central.valor)
print("rama izq:", central.izq.valor)
print("rama der:", central.der.valor)
