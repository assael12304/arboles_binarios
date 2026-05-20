# Ejercicio 9 - Analisis: funcion altura
#
# ERROR IDENTIFICADO:
# La funcion suma las alturas de ambas ramas en lugar de
# tomar la mayor:
#   return 1 + altura(nodo.izquierdo) + altura(nodo.derecho)
#
# La altura de un arbol es la longitud del camino mas largo
# desde la raiz hasta una hoja, no la suma de todos los caminos.
#
# TRAZA en arbol [10, 5, 15, 3]:
#   altura(3)  = 1 + 0 + 0 = 1
#   altura(5)  = 1 + 1 + 0 = 2
#   altura(15) = 1 + 0 + 0 = 1
#   altura(10) = 1 + 2 + 1 = 4  <- incorrecto
#
# La altura real es 3 (camino: 10 -> 5 -> 3).
# CORRECCION: reemplazar la suma por max().

class Vertice:
    def __init__(self, valor):
        self.valor = valor
        self.izq   = None
        self.der   = None

class BST:
    def __init__(self):
        self.raiz = None

    def agregar(self, valor):
        if self.raiz is None:
            self.raiz = Vertice(valor)
        else:
            self._ag(self.raiz, valor)

    def _ag(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izq is None:
                nodo.izq = Vertice(valor)
            else:
                self._ag(nodo.izq, valor)
        elif valor > nodo.valor:
            if nodo.der is None:
                nodo.der = Vertice(valor)
            else:
                self._ag(nodo.der, valor)


def altura(nodo):
    if nodo is None:
        return 0
    # correccion: max en lugar de suma
    return 1 + max(altura(nodo.izq), altura(nodo.der))


arbol = BST()
for n in [10, 5, 15, 3]:
    arbol.agregar(n)

print(altura(arbol.raiz))  # 3
