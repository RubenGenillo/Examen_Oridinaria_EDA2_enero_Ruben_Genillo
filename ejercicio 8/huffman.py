from colaPrioridad import Cola
from arbolBinario import nodoArbol
setattr(nodoArbol, 'peso', None)

def crearDecodificador(listaLetras, listaPeso):
    cola = Cola()
    for i in range(len(listaLetras)):
        nodo = nodoArbol(listaLetras[i])
        nodo.peso = listaPeso[i]
        cola.añadir(nodo, listaPeso[i]) 
    while(cola.tamanio > 1):
        nodo1 = cola.atender()
        nodo2 = cola.atender()
        nodo = nodoArbol(None)
        nodo.izq = nodo1[0]
        nodo.der = nodo2[0]
        peso = nodo1[1] + nodo2[1]
        #nodo.peso = peso
        cola.añadir(nodo, peso)
    return cola.primero.info[0]

def decodificar(decodificador, texto):
    buscador = decodificador
    cadena = ""
    for i in texto:
        if i == "0":
            if buscador.izq is not None:
                buscador = buscador.izq
            else:
                cadena += buscador.info
                buscador = decodificador.izq
        else:
            if buscador.der is not None:
                buscador = buscador.der
            else:
                cadena += buscador.info
                buscador = decodificador.der
    cadena += buscador.info
    return cadena

def generar(decodificador, lista, texto=''):
    if decodificador.info is None:
        generar(decodificador.izq, lista, texto + '0')
        generar(decodificador.der, lista, texto + '1')
    else:
        lista.append((decodificador.info, texto))

def codificar(decodificador, texto):
    tabla = []
    generar(decodificador, tabla)
    resultado = ""
    for i in texto:
        for j in tabla:
            if i == j[0]:
                resultado += j[1]
    return resultado

