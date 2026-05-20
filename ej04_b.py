# Ejercicio 4 - Completa el metodo insertar

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
            # primer elemento: se convierte en la raiz del arbol
            self.raiz = Vertice(valor)
        else:
            self._agregar_rec(self.raiz, valor)

    def _agregar_rec(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izq is None:
                # encontramos el lugar: insertamos a la izquierda
                nodo.izq = Vertice(valor)
            else:
                # seguimos buscando hacia abajo por la izquierda
                self._agregar_rec(nodo.izq, valor)
        elif valor > nodo.valor:
            if nodo.der is None:
                # encontramos el lugar: insertamos a la derecha
                nodo.der = Vertice(valor)
            else:
                # seguimos buscando hacia abajo por la derecha
                self._agregar_rec(nodo.der, valor)
        # valor igual al nodo: duplicado, no se agrega

arbol = BST()
for n in [10, 5, 15, 3, 7, 12, 20]:
    arbol.agregar(n)

print(arbol.raiz.valor)       # 10
print(arbol.raiz.izq.valor)   # 5
print(arbol.raiz.der.valor)   # 15
