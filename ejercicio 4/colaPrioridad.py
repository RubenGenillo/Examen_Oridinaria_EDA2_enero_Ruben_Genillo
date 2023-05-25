class Nodo(object):
    info,sig = None, None

class Cola(object):
    def __init__(self):
        self.tamanio = 0
        self.primero, self.ultimo = None, None

    def añadir(cola, info, prioridad=0):
        nuevo = Nodo()
        nuevo.info = (info, prioridad)
        if cola.primero is None or cola.primero.info[1] > prioridad:
         nuevo.sig = cola.primero
         cola.primero = nuevo        
        else:
         anterior = cola.primero
         siguiente = cola.primero.sig
         while True:
            if siguiente is not None:
             if siguiente.info[1] <= prioridad:
                anterior = siguiente
                siguiente = siguiente.sig
             else:
                break
            else:
               cola.ultimo = nuevo
               break
         nuevo.sig = siguiente
         anterior.sig = nuevo
        cola.tamanio += 1

    def atender(cola):
        dato = cola.primero.info
        cola.primero = cola.primero.sig
        if cola.primero is None:
            cola.ultimo = None
        cola.tamanio -= 1
        return dato

    def cola_vacia(cola):
        return cola.primero is None

    def mostrar_Primero(cola):
       return cola.primero.info
    
    def colaTamanio(cola):
        return cola.tamanio
    
    def mover_al_final(cola):
        dato = cola.atender()
        cola.añadir(dato[0], dato[1])
        return dato


    # def Barrido(cola):
    #     veces = cola.tamanio
    #     for i in range(veces):
    #        print(cola.mover_al_final())


if __name__ == "__main__":
   prueba = Cola()
   prueba.añadir(1, 1)
   prueba.añadir(2, 2)
   prueba.añadir(3, 3)
   prueba.añadir(4, 2)
   print(prueba.atender())
   print(prueba.atender())
   print(prueba.atender())