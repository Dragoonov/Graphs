class BinaryHeap:

    def __init__(self):
        self.heap = [(-1, -1)]

    def insert(self, e, p):
        self.heap.append((e, p))
        self._up_heap(-1)

    def find_min(self):
        return self.heap[1]

    def del_min(self):
        var = self.heap[1]
        self.heap[1] = self.heap.pop()
        self._down_heap(1)
        return var

    def _up_heap(self, i):
        if i > 0:
            key = self.heap[i]
            parent = int(i / 2)
            while (parent > 0) and (self.heap[parent][1] > key[1]):
                self.heap[i] = self.heap[parent]
                i = parent
                parent /= 2
            self.heap[i] = key

    def _down_heap(self, i):
        left = 2 * i
        right = 2 * i + 1
        if left <= len(self.heap) and self.heap[left][1] < self.heap[i][1]:
            minimum = left
        else:
            minimum = i
        if right <= len(self.heap) and self.heap[right][1] < self.heap[minimum][1]:
            minimum = right
        if minimum != i:
            self.heap[i], self.heap[minimum] = self.heap[minimum], self.heap[i]
            self._down_heap(minimum)
