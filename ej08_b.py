# Ejercicio 8 - Analisis: funcion buscar
#
# ERROR IDENTIFICADO:
# Falta el caso base para cuando nodo es None.
# La funcion asume que siempre recibe un nodo valido,
# pero cuando el valor buscado no existe, la recursion
# eventualmente llega a None e intenta leer None.dato,
# lo que genera AttributeError.
#
# TRAZA buscando 99 en arbol [10, 5, 15]:
#   buscar(raiz=10, 99) -> 99 > 10 -> buscar(15, 99)
#   buscar(nodo=15, 99) -> 99 > 15 -> buscar(None, 99)
#   buscar(nodo=None, 99) -> None.dato -> AttributeError
#
# CORRECCION: verificar si nodo es None antes de acceder
# a sus atributos y retornar False en ese caso.

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


def buscar(nodo, valor):
    # caso base corregido: nodo vacio significa que no existe
    if nodo is None:
        return False
    if nodo.valor == valor:
        return True
    if valor < nodo.valor:
        return buscar(nodo.izq, valor)
    else:
        return buscar(nodo.der, valor)


arbol = BST()
for n in [10, 5, 15]:
    arbol.agregar(n)

print(buscar(arbol.raiz, 5))   # True
print(buscar(arbol.raiz, 99))  # False
