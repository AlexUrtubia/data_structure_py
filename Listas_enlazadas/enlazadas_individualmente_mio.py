class Lista_enl:
    def __init__(self):
        self.primero = None
    
    def definir_primero(self, valor): # Para definir el primero
        nuevo_nodo = Nodo(valor) # Creo un nodo nuevo
        actual_primero = self.primero # guardo el primero de la lista en una variable auxiliar
        nuevo_nodo.proximo = actual_primero #indico que el siguiente o vecino del nodo nuevo recién creado es el anterior primero de la lista
        self.primero = nuevo_nodo # se define que el primero de la lista será el nuevo nodo recién creado
        return self
        
    def definir_ultimo(self, valor): # Para definir el último
        if self.primero == None: # Antes de definir el último se revisa si es que existen otros elementos en la lista
            self.definir_primero(valor) # Se define como primero el nuevo valor
            return self # No se ejecuta el resto del código
        nuevo_nodo = Nodo(valor) # Se crea un nodo nuevo instanciando la clase Nodo
        recorrer = self.primero # Se define una variable que recorrerá toda la lista, empezando por el primero 
        while recorrer.proximo != None: # Si es que existe un vecino, se sigue iterando
            recorrer = recorrer.proximo # Recorrer pasa desde el valor actual, al siguiente (el primero en la priemra iteración al segundo) 
        recorrer.proximo = nuevo_nodo  # Cuando el vecino siguiente es igual a None, es decir no existe, el siguiente vecino se define cmo el nuevo nodo creado
        return self
    
    def imprimir_valores(self):
        recorrer = self.primero
        while recorrer != None:
            print(recorrer.valor)
            recorrer = recorrer.proximo # La iteración avanza desde el valor actual al sguiente
        return self
        

class Nodo: 
    def __init__(self, valor):
        self.valor = valor 
        self.proximo = None
        

lista1=Lista_enl().definir_primero("PO").definir_primero("OLA").definir_ultimo("OLVIDONA").imprimir_valores()