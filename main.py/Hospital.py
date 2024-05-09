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


class MinHeap:
    def __init__(self, value):
        self.value = value
        self.leftchild = None
        self.rightchild = None
        self.parent = None

def insert(rootNode, value):
    if rootNode is None:
        return MinHeap(value)
    
    queue = [rootNode]
    while queue:
        current = queue.pop(0)
        
        if current.leftchild is None:
            current.leftchild = MinHeap(value)
            current.leftchild.parent = current
            ParentControl(current.leftchild)
            break
        elif current.rightchild is None:
            current.rightchild = MinHeap(value)
            current.rightchild.parent = current
            ParentControl(current.rightchild)
            break
        else:
            # Agregar a la cola los nodos hijos actuales
            queue.append(current.leftchild)
            queue.append(current.rightchild)
    
    return rootNode 

def searchNode(rootNode, value):
  if rootNode is None:
    return

  if value < rootNode.value:
    if rootNode.leftchild is not None:
      if rootNode.leftchild.value == value:
        return "el nodo con valor {} SI fue encontrado".format(value)
      return searchNode(rootNode.leftchild,value)
    else:
      return "el nodo con valor {} NO fue encontrado".format(value)
  else:
    if rootNode.rightchild is not None:
      if rootNode.rightchild.value == value:
        return "el nodo con valor {} SI fue encontrado".format(value)
      return searchNode(rootNode.rightchild,value)
    else:
      return "el nodo con valor {} NO fue encontrado".format(value)
    
# Método para mantener la propiedad del min-heap después de insertar un nuevo nodo
def ParentControl(node):
    while node.parent is not None and node.value < node.parent.value:
        node.value, node.parent.value = node.parent.value, node.value
        node = node.parent
    return node

# Método para imprimir el árbol
def printTree(node, prefix="", is_left=True):
    if not node:
        return

    printTree(node.rightchild, prefix + ("│    " if is_left else "     "), False)
    print(prefix + ("└── " if is_left else "┌── ") + str(node.value))
    printTree(node.leftchild, prefix + ("     " if is_left else "│    "), True)

def deleteNode(rootNode, value):
    if rootNode is None:
        return None

    if value < rootNode.value:
        rootNode.leftchild = deleteNode(rootNode.leftchild, value)
    elif value > rootNode.value:
        rootNode.rightchild = deleteNode(rootNode.rightchild, value)
    else:
        # Caso 1: No tiene hijos
        if rootNode.leftchild is None and rootNode.rightchild is None:
            return None
        # Caso 2: Tiene ambos hijos
        elif rootNode.leftchild is not None and rootNode.rightchild is not None:
            tempNode = LastNode(rootNode.leftchild)
            rootNode.value = tempNode.value
            rootNode.leftchild = deleteNode(rootNode.leftchild, tempNode.value)
        # Caso 3: Tiene solo un hijo
        elif rootNode.leftchild is not None:
            return rootNode.leftchild
        else:
            return rootNode.rightchild

    return rootNode

def removeMin(rootNode):
    if rootNode is None:
        return None
    
    if rootNode.leftchild is None and rootNode.rightchild is None:
        return None
    
    min_value = rootNode.value
    
    last_node = LastNode(rootNode)
    
    rootNode.value = last_node.value
    
    if last_node.parent.leftchild == last_node:
        last_node.parent.leftchild = None
    else:
        last_node.parent.rightchild = None
    
    verificarMinHeap(rootNode)
    
    return min_value

def LastNode(rootNode):
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

def verificarMinHeap(node):
    while node.leftchild is not None or node.rightchild is not None:
        if node.leftchild is not None and node.rightchild is not None:
            if node.leftchild.value < node.rightchild.value:
                min_child = node.leftchild
            else:
                min_child = node.rightchild
        elif node.leftchild is not None:
            min_child = node.leftchild
        else:
            min_child = node.rightchild
        
        if node.value > min_child.value:
            node.value, min_child.value = min_child.value, node.value
            node = min_child
        else:
            break

root = None
root = insert(root, 2)
root = insert(root, 1)
root = insert(root, 3)
root = insert(root, 4)
root = insert(root, 3)
root = insert(root, 4)

print("Árbol de min-heap original:")
printTree(root)

buscar = searchNode(root, 3)
print (buscar)


remover=deleteNode(root, 2)
printTree(root)