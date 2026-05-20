# Ejercicio 7 - Analisis: metodo insertar
#
# ERROR IDENTIFICADO:
# En el bloque que maneja valores MENORES que el nodo actual,
# cuando el hijo izquierdo ya existe, la llamada recursiva
# pasa nodo.derecho en lugar de nodo.izquierdo:
#
#   else:
#       self._insertar_rec(nodo.derecho, dato)  <- incorrecto
#
# Si el valor es menor, la busqueda debe continuar por la
# izquierda. Al pasar nodo.derecho se baja por el lado
# contrario, insertando el valor en una posicion incorrecta.
#
# IMPACTO:
# El arbol pierde la propiedad BST silenciosamente.
# No hay error de ejecucion, pero los valores quedan mal
# ubicados y operaciones como buscar o recorrer darian
# resultados incorrectos.

class Vertice:
    def __init__(self, valor):
        self.valor = valor
        self.izq   = None
        self.der   = None

class BST:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Vertice(valor)
        else:
            self._insertar_rec(self.raiz, valor)

    def _insertar_rec(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izq is None:
                nodo.izq = Vertice(valor)
            else:
                # correccion: bajar por izq, no por der
                self._insertar_rec(nodo.izq, valor)
        elif valor > nodo.valor:
            if nodo.der is None:
                nodo.der = Vertice(valor)
            else:
                self._insertar_rec(nodo.der, valor)

arbol = BST()
arbol.insertar(10)
arbol.insertar(5)
arbol.insertar(3)
print(arbol.raiz.izq.izq.valor)  # 3
