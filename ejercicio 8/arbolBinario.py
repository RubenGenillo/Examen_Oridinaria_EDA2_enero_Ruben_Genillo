from cola import Cola

class nodoArbol():
    def __init__(self, info):
        self.info = info
        self.izq = None
        self.der = None

#como hago para llamar recursivamente a un metodo en python

#solo sirve para valores numericos

#la razon por la que esta hecho de esta manera, es porque se llama recursivamente (y así es más rápido)
    
    def insertar_nodo(raiz, dato):
        if raiz is None:
            raiz = nodoArbol(dato)
        elif dato < raiz.info:
            raiz.izq = nodoArbol.insertar_nodo(raiz.izq, dato)
        else:
            raiz.der = nodoArbol.insertar_nodo(raiz.der, dato)
        return raiz


    #nunca borra el primero
    #que pasa si se insertan dos nodos con el mismo valor(y quieres borrar el que esta a mayor nivel)???
    #me gustaria que me lo explicara un poco
    def eliminar_nodo(raiz, clave):
        x = None
        if(raiz is not None):
            if(clave < raiz.info):
                raiz.izq, x = nodoArbol.eliminar_nodo(raiz.izq, clave)
            elif(clave > raiz.info):
                raiz.der, x = nodoArbol.eliminar_nodo(raiz.der, clave)
            else:
                x = raiz.info
                if(raiz.izq is None):
                    raiz = raiz.der
                elif(raiz.der is None):
                    raiz = raiz.izq
                else:
                    #aqui deberia ser raiz en vez de raiz.izq???
                    raiz.izq, aux = nodoArbol.remplazar(raiz.izq)
                    raiz.info = aux.info
        return raiz, x
    

    def arbol_vacio(raiz):
        return raiz == None

#llamo al metodo como si lo cogiera de la clase
    def remplazar(raiz):
        aux = None
        if(raiz.der is None):
            aux = raiz
            raiz = raiz.izq
        else:
            raiz.der, aux = nodoArbol.remplazar(raiz.der)
        return raiz, aux    

#añado la estructura de cola??? (le pregunto que tal, ya que le cambie un par de cosas))
    def por_nivel(raiz):
        pendientes = Cola()
        pendientes.añadir(raiz)
        while not pendientes.cola_vacia():
            nodo = pendientes.atender()
            print(nodo.info)
            if nodo.izq is not None:
                pendientes.añadir(nodo.izq)
            if nodo.der is not None:
                pendientes.añadir(nodo.der)

    def buscar(raiz, clave):
        pos = None
        if (raiz.info is not None):
            if(raiz.info == clave):
                pos = raiz
            elif(clave < raiz.info):
                pos = nodoArbol.buscar(raiz.izq, clave)
            else:
                pos = nodoArbol.buscar(raiz.der, clave)
        return pos
    
    def inorden(raiz):
        if raiz is not None:
            nodoArbol.inorden(raiz.izq)
            print(raiz.info)
            nodoArbol.inorden(raiz.der)

    def preorden(raiz):
        if raiz is not None:
            print(raiz.info)
            nodoArbol.preorden(raiz.izq)
            nodoArbol.preorden(raiz.der)


    def postorden(raiz):
        if raiz is not None:
            nodoArbol.postorden(raiz.der)
            print(raiz.info)
            nodoArbol.postorden(raiz.izq)
            


if __name__ == "__main__":
    Prueba = nodoArbol(0)
    Prueba.insertar_nodo(1)
    Prueba.insertar_nodo(1)
    

    Prueba.por_nivel()
