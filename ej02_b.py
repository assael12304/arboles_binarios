# Ejercicio 2 - Construyendo un arbol paso a paso

class Vertice:
    def __init__(self, valor):
        self.valor = valor
        self.izq   = None
        self.der   = None

# construimos el arbol nivel por nivel

# nivel 0: raiz
central = Vertice(10)

# nivel 1
central.izq = Vertice(5)
central.der = Vertice(15)

# nivel 2: hijos de 5
central.izq.izq = Vertice(3)
central.izq.der = Vertice(7)

# nivel 2: hijos de 15
central.der.izq = Vertice(12)
central.der.der = Vertice(20)

# verificacion del punto e)
# central.izq.valor         deberia imprimir 5
# central.der.izq.valor     deberia imprimir 12
print(central.izq.valor)         # 5
print(central.der.izq.valor)     # 12
