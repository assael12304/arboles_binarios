# Ejercicio 5 - Buscar, altura y contar nodos

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

    def existe(self, valor):
        return self._existe_rec(self.raiz, valor)

    def _existe_rec(self, nodo, valor):
        # si llegamos a None el valor no esta en el arbol
        if nodo is None:
            return False
        # lo encontramos
        if nodo.valor == valor:
            return True
        # valor mas pequeno: buscar en rama izquierda
        elif valor < nodo.valor:
            return self._existe_rec(nodo.izq, valor)
        # valor mas grande: buscar en rama derecha
        else:
            return self._existe_rec(nodo.der, valor)


def profundidad(nodo):
    # nodo vacio no aporta nivel
    if nodo is None:
        return 0
    rama_izq = profundidad(nodo.izq)
    rama_der = profundidad(nodo.der)
    # tomamos la rama mas profunda y sumamos el nodo actual
    return 1 + max(rama_izq, rama_der)


def total_nodos(nodo):
    if nodo is None:
        return 0
    # nodo actual + todos los de sus dos subarboles
    return 1 + total_nodos(nodo.izq) + total_nodos(nodo.der)


# Sin el caso base 'if nodo is None', la recursion no sabria
# cuando parar y terminaria con un error al intentar leer
# atributos de un objeto que no existe.

arbol = BST()
for n in [10, 5, 15, 3, 7, 12, 20]:
    arbol.agregar(n)

print(arbol.existe(7))          # True
print(arbol.existe(99))         # False
print(profundidad(arbol.raiz))  # 3
print(total_nodos(arbol.raiz))  # 7
