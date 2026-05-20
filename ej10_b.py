# Ejercicio 10 - Aplicacion real: organigrama universitario
#
# Parte A - Explicacion:
# Una universidad tiene una jerarquia natural de autoridad.
# La raiz es el rector, los nodos internos son decanos
# y directores de programa, y las hojas son los docentes.
# El recorrido inorden permite listar todos los miembros
# en orden alfabetico. La busqueda permite ubicar a una
# persona dentro del organigrama rapidamente.
#
# Parte B - Codigo

class Cargo:
    def __init__(self, nombre, rol):
        self.nombre = nombre   # nombre de la persona
        self.rol    = rol      # cargo que ocupa
        self.izq    = None
        self.der    = None


def listar_personal(nodo):
    if nodo is None:
        return
    listar_personal(nodo.izq)
    print(f"  {nodo.rol:25} -> {nodo.nombre}")
    listar_personal(nodo.der)


def buscar_cargo(nodo, nombre):
    if nodo is None:
        return None
    if nodo.nombre == nombre:
        return nodo.rol
    resultado = buscar_cargo(nodo.izq, nombre)
    if resultado:
        return resultado
    return buscar_cargo(nodo.der, nombre)


# construccion del organigrama
rector              = Cargo("Dr. Ramirez",  "Rector")
rector.izq          = Cargo("Dra. Torres",  "Decana Ingenieria")
rector.der          = Cargo("Dr. Morales",  "Decano Ciencias")

rector.izq.izq      = Cargo("Ing. Perez",   "Director Sistemas")
rector.izq.der      = Cargo("Ing. Gomez",   "Director Civil")
rector.der.izq      = Cargo("Dr. Vargas",   "Director Biologia")

print("Personal de la universidad:")
listar_personal(rector)

print()
nombre_buscar = "Ing. Gomez"
cargo = buscar_cargo(rector, nombre_buscar)
print(f"{nombre_buscar} ocupa el cargo: {cargo}")
