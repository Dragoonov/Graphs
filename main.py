
class BinaryHeap:

    def __init__(self):
        self.heap = [[-1, -1]]

    def insert(self, e, p):
        self.heap.append([e, p])
        self._up_heap(len(self.heap) - 1)

    def find_min(self):
        return self.heap[1]

    def del_min(self):
        var = self.heap[1]
        if len(self.heap) > 2:
            self.heap[1] = self.heap.pop()
            self._down_heap(1)
        return var

    def _up_heap(self, i):
        if i > 0:
            key = self.heap[i]
            parent = i // 2
            while (parent > 0) and (self.heap[parent][1] > key[1]):
                self.heap[i] = self.heap[parent]
                i = parent
                parent = parent // 2
            self.heap[i] = key

    def _down_heap(self, i):
        left = 2 * i
        right = 2 * i + 1
        if left <= len(self.heap) - 1 and self.heap[left][1] < self.heap[i][1]:
            minimum = left
        else:
            minimum = i
        if right <= len(self.heap) - 1 and self.heap[right][1] < self.heap[minimum][1]:
            minimum = right
        if minimum != i:
            self.heap[i], self.heap[minimum] = self.heap[minimum], self.heap[i]
            self._down_heap(minimum)


def find_vertex(e, data):
    for value in data:
        if value[0] == e:
            return value
    return None


def Prim(data, start):
    tree = [(data[start][0], None)]
    heap = BinaryHeap()
    for value in data[start][1]:
        heap.insert(value[0], value[1])
    while len(tree) < len(data):
        minimal_node = heap.del_min()
        if find_vertex(minimal_node[0], tree) is None:
            tree.append((minimal_node[0], minimal_node[1]))
            vertex = find_vertex(minimal_node[0], data)
            for adjacent in vertex[1]:
                if find_vertex(adjacent[0], tree) is None:
                    heap.insert(adjacent[0], adjacent[1])
    return tree


graph1 = [
    (0, [(3, 13), (2, 13), (1, 24), (4, 22)]),
    (1, [(3, 13), (0, 24), (2, 22), (4, 13)]),
    (2, [(0, 13), (3, 19), (1, 22), (4, 14)]),
    (3, [(0, 13), (2, 19), (4, 19), (1, 13)]),
    (4, [(1, 13), (3, 19), (2, 14), (0, 22)])
]

graph2 = [
    (0, [(2, 12), (1, 8)]),
    (1, [(0, 8), (2, 13), (3, 25), (4, 9)]),
    (2, [(0, 12), (1, 13), (6, 21), (3, 14)]),
    (3, [(2, 14), (1, 25), (4, 20), (5, 8), (7, 12), (8, 16), (6, 12)]),
    (4, [(1, 9), (3, 20), (5, 19)]),
    (5, [(4, 19), (3, 8), (7, 11)]),
    (6, [(2, 21), (3, 12), (8, 11)]),
    (7, [(8, 9), (3, 12), (5, 11)]),
    (8, [(6, 11), (3, 16), (7, 9)])
]

graph3 = [
    (0, [(2, 75), (1, 9)]),
    (1, [(0, 9), (2, 95), (3, 19), (4, 42)]),
    (2, [(0, 75), (1, 95), (3, 51)]),
    (3, [(2, 51), (1, 19), (4, 31)]),
    (4, [(1, 42), (3, 31)])
]

print(Prim(graph3, 0))
