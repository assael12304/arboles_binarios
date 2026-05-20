# Ejercicio 6 - Recorrido inorden, minimo y maximo

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


def inorden(nodo, acumulado=None):
    if acumulado is None:
        acumulado = []   # lista nueva en cada llamada principal
    if nodo is not None:
        inorden(nodo.izq, acumulado)    # visitar izquierda primero
        acumulado.append(nodo.valor)    # registrar nodo actual
        inorden(nodo.der, acumulado)    # visitar derecha al final
    return acumulado


def minimo(nodo):
    # el valor mas pequeno siempre esta en el extremo izquierdo
    if nodo.izq is None:
        return nodo.valor
    return minimo(nodo.izq)


def maximo(nodo):
    # el valor mas grande siempre esta en el extremo derecho
    if nodo.der is None:
        return nodo.valor
    return maximo(nodo.der)


# El inorden siempre da orden ascendente en un BST porque
# la regla de insercion garantiza que la rama izquierda
# contiene solo menores y la rama derecha solo mayores.
# Visitar izquierda primero equivale a listar de menor a mayor.

arbol = BST()
for n in [10, 5, 15, 3, 7, 12, 20]:
    arbol.agregar(n)

print(inorden(arbol.raiz, []))  # [3, 5, 7, 10, 12, 15, 20]
print(minimo(arbol.raiz))       # 3
print(maximo(arbol.raiz))       # 20
