import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        heapq.heappush(self.heap, value)

    def extract_min(self):
        if self.heap:
            return heapq.heappop(self.heap)
        else:
            return None

    def get_min(self):
        if self.heap:
            return self.heap[0]
        else:
            return None

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0
    
    def printTree(self, node=None, prefix="", is_left=True):
      if node is None:
          node = self

      if not node:
          return

      if node.value:
          self.printTree(node.value, prefix + ("│    " if is_left else "    "), False)

      print(prefix + ("└── " if is_left else "┌── ") + str(node.value))

      if node.leftchild:
          self.printTree(node.leftchild, prefix + ("     " if is_left else "│   "), True)


# Ejemplo de uso
heap = MinHeap()
heap.insert(10)
heap.insert(5)
heap.insert(20)
heap.insert(3)

heap.printTree()

print("Mínimo:", heap.get_min())  # Output: 3
print("Extraer mínimo:", heap.extract_min())  # Output: 3
print("Nuevo mínimo:", heap.get_min())  # Output: 5
print("Tamaño del heap:", heap.size())  # Output: 3
