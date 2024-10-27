class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class Arbol:
    def __init__(self):
        self.raiz = None

    def agregar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._agregar_recursivo(self.raiz, valor)

    def _agregar_recursivo(self, nodo_actual, valor):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = Nodo(valor)
            else:
                self._agregar_recursivo(nodo_actual.izquierdo, valor)
        else:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = Nodo(valor)
            else:
                self._agregar_recursivo(nodo_actual.derecho, valor)

    def imprimir_en_orden(self):
        self._imprimir_en_orden_recursivo(self.raiz)

    def _imprimir_en_orden_recursivo(self, nodo_actual):
        if nodo_actual is not None:
            self._imprimir_en_orden_recursivo(nodo_actual.izquierdo)
            print(nodo_actual.valor)
            self._imprimir_en_orden_recursivo(nodo_actual.derecho)

# Ejemplo de uso:
arbol = Arbol()
arbol.agregar(10)
arbol.agregar(5)
arbol.agregar(15)
arbol.agregar(3)
arbol.agregar(7)

print("Elementos del árbol en orden:")
arbol.imprimir_en_orden()
