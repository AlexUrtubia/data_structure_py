class SList: #Orden Lista 
    def __init__(self):
        self.head = None
        
    def add_to_front(self, val):	# Agregar un valor como primero de la lista
        new_node = SLNode(val)  #Instancia la clase SLNode y crea un nodo con un valor
        current_head = self.head # salva la cabecera actual en una variable, ya que si no se guarda,
                                # El valor que está actual% primero de la lista, se sobreescribe y se perderá
        new_node.next = current_head	# Cambia el atributo "next" de la clase SLNode desde "None" hacia el actual valor de cabecera
        #Coloca el proximo nodo en la lista de la cabecera actual, como si fuera un auxiliar
        self.head = new_node	# Coloca la lista de la cabecera al nodo que se creó en el paso anterior
                                # El nuevo nodo siempre terminará siendo el primero de la lista
        return self	                # return self para permitir el encadenamiento
    
    def print_values(self): #Funcion que recorre la lista e imprime sus valores
        runner = self.head # "runner" realiza la función de un contador, comienza en la cabecera
        while (runner != None): # Mientras que la cabezera sea distinta de "None", es decir mientras exista algún valor en la lista, itera
            # Llega hasta el último nodo, y el valor de este vecino será "None" por no estar definido, por ende defa de iterar
            print(runner.value) # Imprime el valor del contador, es decir del nodo actual
            runner = runner.next 	# Establecer el contador como el valor de su vecino
        return self             # Una vez que el bucle está terminado, regrese a sí mismo para permitir el encadenamiento
	
    def add_to_back(self, val):
        if self.head == None:	# si la lista está vacia
            self.add_to_front(val)	# ejecuta el método add_to_front
            return self	# el resto de esta función no sucederá si se agrega el nuevo nodo al frente
        new_node = SLNode(val)  # Instancia un nuevo nodo
        runner = self.head  # El contador comienza en el encabezado
        while (runner.next != None): # igual que el anterior, mientras que exista un vecino, sigue la iteración
            runner = runner.next    # El contador avanza hasta el vecino
        runner.next = new_node	# Saliendo de la iteración, el siguiente vecino será el nuevo nodo, es decir, el último de la lista
        return self # retorna self para permitir el encadenamiento
        
    def remove_from_front(self):
        runner = self.head
        self.head = runner.next
        return self
    
    def remove_from_back(self):
        if(self.head!=None and self.head.next!=None): # Si es que existe un primer valor y un vecino de este, itera
            runner = self.head
            while(runner.next.next != None):    # Hasta que el siguiente del siguiente sea none (+2 del penúltimo) 
                runner = runner.next
            runner.next=None
        elif(self.head.next==None):        # Otra condición, si es que el valor siguiente al primer nodo no existe
            self.head.value=None            # El valor del primero se convierte en None
        return self
        
#     https://runestone.academy/runestone/static/pythoned/BasicDS/ImplementacionDeUnaListaNoOrdenadaListasEnlazadas.html
	
    def remove_val(self, val):  # ELiminar nodo con determinado valor
        runner = self.head  # runner siempre comienza en el primer valor
		#Primer nodo eliminado 
        if runner.value == val: # Si runner es el valor indicado, se sobreescribe con el siguinte
            self.head = runner.next
            return self
        #Eliminar el nodo con el valor en medio de la lista
        while (runner.next.value != val):   # Mientras que el valor del vecino de runner sea distinto del valor, itera
            runner = runner.next
        temp = runner.next  # Cuando el valor del vecino es el valor buscadom crea una variable temporal con el valor buscado
        runner.next = temp.next # e indica que el valor será reemplazado por el vecino siguiente
        return self

    def insert_at(self, val, n):    # Inserta nodo en posición n, con valor val
        runner = self.head
        if n == 0:      # Si n es 0, es decir el primer valor, simplemente llama al método addtofront
            self.add_to_front(val)
        else:
            contador = 1    # Si no inicia un contador que hará avanzar al runner mientras que su valor sea menor a n
            while contador < n:
                runner = runner.next    # runner se transforma en el sgte
                contador += 1   # el contador aumenta en 1
            temp = runner.next  # Cuando el contador deja de ser menor a n, crea un aux que tiene un value del nodo ubicado en n
            nuevo = SLNode(val) # crea un nuevo nodo con el valor de val
            runner.next = nuevo # Indica que el siguiente del vecino, es decir el índice donde se agrega el valor, vale nuevo
            nuevo.next = temp   # Finalmente indica que el siguiente a nuevo, será el valor de temp, es decir el valor del nodo que estaba en el índice n
        return self
    
class SLNode:   #Creación de nodos
    def __init__(self, val):
        self.value = val # EL nuevo valor contiene: un valor
        self.next = None    # Y un vecino-siguiente que por defecto queda declarado como None
            
my_list = SList()	# crear una nueva instancia de una lista
my_list.add_to_front("son").add_to_front("Las listas enlazadas").add_to_back("bacanes!").print_values()
# la saalida deberia ser:
# Listas enlazadas
# son
# divertidas!
my_list.remove_from_back().print_values()
lista1 = SList().add_to_front("1").add_to_back("2").add_to_back("3").add_to_back("4").add_to_back("5").print_values()
print("")
lista1.remove_val("5").print_values()
print("")
lista1.insert_at("Nuevo",4).print_values()