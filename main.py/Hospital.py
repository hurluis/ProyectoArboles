class Node:
  __slots__ = 'value', 'next'

  def __init__(self, value):
    self.value = value
    self.next = None

  def __str__(self):
    return str(self.value)

class LinkedList:

  def __init__(self):
    self.head = None
    self.tail = None

  def __iter__(self):
    curNode = self.head
    while curNode:
      yield curNode
      curNode = curNode.next

  def __str__(self):
    result = [str(x.value) for x in self]
    return ' '.join(result)

class queue:

  def __init__(self):
    self.linkedlist = LinkedList()

  def __str__(self):
    result = [str(x.value) for x in self.queue]
    return ' '.join(result)

  def is_empty(self):
    return self.linkedlist.head == None

  def enqueue(self, e):
    new_node = Node(e)
    if self.linkedlist.head == None:
      self.linkedlist.head = new_node
      self.linkedlist.tail = new_node
    else:
      new_node.next = None
      self.linkedlist.tail.next = new_node
      self.linkedlist.tail = new_node

  def dequeue(self):
    if self.is_empty():
      return "No hay elementos en la lista"
    else:
      popped_node = self.linkedlist.head
      if self.linkedlist.head == self.linkedlist.tail:
        self.linkedlist.head = None
        self.linkedlist.tail = None
      else:
        self.linkedlist.head = self.linkedlist.head.next
      popped_node.next = None
      return popped_node


class Hospital:
    def __init__(self, value=None):
        self.value = value
        self.leftchild = None
        self.rightchild = None
        self.parent = None
        self.length = 0 
        self.queue = queue()
        self.Node = Node(value)  



    def insert(self, value):
        if value is None:
            return  

        if self.value is None:
            self.value = value
            self.length = 1 
        else:
            if self.leftchild is None:
                new_node = Hospital(value)
                new_node.parent = self
                self.leftchild = new_node
                self.length += 1  
                self.queue.enqueue(new_node)
            elif self.rightchild is None:
                new_node = Hospital(value)
                new_node.parent = self
                self.rightchild = new_node
                self.length += 1  
                self.queue.enqueue(new_node)
            else:
                if self.leftchild.length <= self.rightchild.length:
                    self.leftchild.insert(value)
                    self.length +=1
                else:
                    self.rightchild.insert(value)
                    self.length +=1

        self.verificarMinHeap()

    
        
    

    def searchNode(self, value):
        if self.value is None:
            return "El nodo con valor {} NO fue encontrado".format(value)
                    
        if self.value == value:
            return "El nodo con valor {} SI fue encontrado".format(value)
                    
        if self.leftchild is not None:
            left_result = self.leftchild.searchNode(value)
            if left_result != "El nodo con valor {} NO fue encontrado".format(value):
                return left_result
        
        if self.rightchild is not None:
            right_result = self.rightchild.searchNode(value)
            if right_result != "El nodo con valor {} NO fue encontrado".format(value):
                return right_result
                
        return "El nodo con valor {} NO fue encontrado".format(value)
                
    
    
    def printTree(self, node=None, prefix="", is_left=True):
        if node is None:
            node = self

        if not node:
            return

        if node.rightchild:
            self.printTree(node.rightchild, prefix + ("│    " if is_left else "    "), False)

        print(prefix + ("└── " if is_left else "┌── ") + str(node.value))

        if node.leftchild:
            self.printTree(node.leftchild, prefix + ("     " if is_left else "│   "), True)

    

    def deleteNode(self, value):
        if self.value == value:
            # Caso 1: No tiene hijos
            if self.leftchild is None and self.rightchild is None:
                self.value = None
                self.length -= 1
                return None
            # Caso 2: Tiene ambos hijos
            elif self.leftchild is not None and self.rightchild is not None:
                # Elegir el sucesor inmediato (podría ser también el predecesor inmediato)
                tempNode = self.rightchild
                while tempNode.leftchild is not None:
                    tempNode = tempNode.leftchild
                self.value = tempNode.value
                self.rightchild = self.rightchild.deleteNode(tempNode.value)
                self.verificarMinHeap()
            # Caso 3: Tiene solo un hijo
            elif self.leftchild is not None:
                self.value = self.leftchild.value
                self.leftchild = None
                self.length -= 1
            else:
                self.value = self.rightchild.value
                self.rightchild = None
                self.length -= 1
        else:
            if self.leftchild is not None:
                self.leftchild = self.leftchild.deleteNode(value)
            if self.rightchild is not None:
                self.rightchild = self.rightchild.deleteNode(value)

        return self

    

    def removeMin(self):
        if self.leftchild is None and self.rightchild is None:
            if self.parent is not None:
                if self.parent.leftchild == self:
                    self.parent.leftchild = None
                else:
                    self.parent.rightchild = None
            min_value = self.value
            self.value = None
            self.length -= 1
            return min_value
                
        min_value = self.value
        last_node = self.LastNode(self)
        self.value = last_node.value
        
        if last_node.parent:
            if last_node.parent.leftchild == last_node:
                last_node.parent.leftchild = None
            else:
                last_node.parent.rightchild = None
            self.length -= 1
        else:
            self.value = None
            self.length -= 1
        
        self.verificarMinHeap()
        return min_value


    def LastNode(self, rootNode):
        if rootNode is None:
            return None
        
        queue = [rootNode]
        while queue:
            current = queue.pop(0)
            if current.leftchild is not None:
                queue.append(current.leftchild)
            if current.rightchild is not None:
                queue.append(current.rightchild)
        
        return current



    def verificarMinHeap(self):
        if self.leftchild and self.value > self.leftchild.value:
            self.value, self.leftchild.value = self.leftchild.value, self.value
            self.leftchild.verificarMinHeap()
        if self.rightchild and self.value > self.rightchild.value:
            self.value, self.rightchild.value = self.rightchild.value, self.value
            self.rightchild.verificarMinHeap()




    def MostrarHojas(self):
        Hojas = []
        self.ObtenerHojas(self, Hojas)
        return Hojas   

    def ObtenerHojas(self, node, Hojas):
        if node is None:
            return

        if node.leftchild is None and node.rightchild is None:
            Hojas.append(node.value)

        if node.leftchild:
            self.ObtenerHojas(node.leftchild, Hojas)

        if node.rightchild:
            self.ObtenerHojas(node.rightchild, Hojas)

    #Valor en las hojas
    def encontrarEnHojas(self, numero):
        Current=[]
        for elemento in self.MostrarHojas():
            if elemento ==numero:
                Current.append(elemento)
        return print(len(Current))
    
    #numero presente en el arbol
    def CantidadNumeros(self, elemento):
        if self is None:
            return 0
        almacenador = 1 if self.value == elemento else 0
        contadorIzquiuera = self.leftchild.CantidadNumeros(elemento) if self.leftchild else 0
        condadorDerecha = self.rightchild.CantidadNumeros(elemento) if self.rightchild else 0

        return almacenador +    contadorIzquiuera + condadorDerecha
    
    def mostrarElementosArbol(self):
        elements = []
        if self.leftchild:
            elements.extend(self.leftchild.mostrarElementosArbol())
        elements.append(self.value)
        if self.rightchild:
            elements.extend(self.rightchild.mostrarElementosArbol())
        return elements
    

    def levelOrderTraversal(self):
        if not self:
            return []

        elements = []
        customqueue = queue()
        customqueue.enqueue(self)

        while not customqueue.is_empty():
            current = customqueue.dequeue()
            elements.append(current.value.value)  
            if current.value.leftchild:
                customqueue.enqueue(current.value.leftchild)

            if current.value.rightchild:
                customqueue.enqueue(current.value.rightchild)

        return print(elements)
    
    def deepestLeftChild(self):
        if not self:
            return None
        
        while self.leftchild:
            self = self.leftchild
        return self

    def deepestRightChild(self):
        if not self:
            return None
        
        while self.rightchild:
            self = self.rightchild
        return self
    
    def deepestValue(self):
        deepest_left = self.deepestLeftChild()
        deepest_right = self.deepestRightChild()

        if deepest_left and deepest_right:
            return deepest_left.value if deepest_left.value > deepest_right.value else deepest_right.value
        elif deepest_left:
            return deepest_left.value
        elif deepest_right:
            return deepest_right.value
        else:
            return self.value

    def DiferenciaAbsolutaMinima(self):
        values = self.mostrarElementosArbol()
        
        minima = float('inf')
        for elemento in range(1, len(values)):
            diferencia = abs(values[elemento] - values[elemento-1])
            if diferencia < minima:
                minima = diferencia
        
        return minima

    def valor_mayor(self):
        current=[]
        iteraciones=0
        while len(self.mostrarElementosArbol()) != iteraciones:
            mayor=float('-inf')
            for elemento in self.mostrarElementosArbol():
                mayor=max(mayor, elemento)
                iteraciones+=1
            current.append(mayor)
        return current

    def calcular_altura(self):
        if not self:
            return 0
        if self.leftchild:
            altura_izquierda = self.leftchild.calcular_altura()
        else:
            altura_izquierda = 0
        if self.rightchild:
            altura_derecha = self.rightchild.calcular_altura()
        else:
            altura_derecha = 0
        return max(altura_izquierda, altura_derecha) + 1
    
    def cantidad_nodos(self):
        current=self.mostrarElementosArbol()
        return len(current)

    def calcsuma_arbol(self):
        suma_total = self.value
    
        if self.leftchild:
            suma_total += self.leftchild.calcsuma_arbol()
        
        if self.rightchild:
            suma_total += self.rightchild.calcsuma_arbol()
        
        return suma_total
    
    def encontrarNivelValor(self, valor, nivel=0):
        if self.value == valor:
            return nivel
        
        nivel_izquierdo = self.leftchild.encontrarNivelValor(valor, nivel + 1) if self.leftchild else 0
        nivel_derecho = self.rightchild.encontrarNivelValor(valor, nivel + 1) if self.rightchild else 0
            
        nivelEncontrado= max(nivel_izquierdo, nivel_derecho)
        return nivelEncontrado
    
    def operacion_arbol(self):
        resultado_izquierdo = 0
        resultado_derecho = 0

        if self.leftchild:
            if self.leftchild.leftchild and self.leftchild.rightchild:
                suma_hijos_izquierdo = self.leftchild.leftchild.calcsuma_arbol() + self.leftchild.rightchild.calcsuma_arbol()
                resultado_izquierdo = suma_hijos_izquierdo * self.leftchild.value
        if self.rightchild:
            if self.rightchild.leftchild and self.rightchild.rightchild:
                suma_hijos_derecho = self.rightchild.leftchild.calcsuma_arbol() + self.rightchild.rightchild.calcsuma_arbol()
                resultado_derecho = suma_hijos_derecho * self.rightchild.value

        resultado = resultado_izquierdo - resultado_derecho
        return resultado
    

hospital = Hospital()
hospital.insert(10)
hospital.insert(5)
hospital.insert(15)
hospital.insert(13)
hospital.insert(7)
hospital.insert(44)
hospital.insert(2)
hospital.insert(1)
hospital.insert(4)


# Print the tree
hospital.printTree()

print(hospital.encontrarNivelValor(15))
"""Hojas = hospital.MostrarHojas()
print("\nHojas:", Hojas)

# Print the tree after getting Hojas
print("\nTree after getting Hojas (should be unchanged):")
hospital.printTree()

hospital.encontrarEnHojas(4)

print(hospital.CantidadNumeros(4))

nodos=hospital.mostrarElementosArbol()
print("\nNodos del arbol: ", nodos)

(hospital.levelOrderTraversal())

print(hospital.deepestRightChild().value)

print(hospital.calcsuma_arbol())

print("Árbol original:")
hospital.printTree()



print("\nÁrbol invertido:")
hospital.printTree()"""
        