import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        #import ipdb; ipdb.set_trace() # breakpoint
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)

if __name__ == '__main__':

    # Tupla de prioridades:
    # (priority, index, item)
    a = (1, 0, Item('foo'))
    b = (-1, 1, Item('bar'))
    c = (1, 2, Item('bar'))
    d = (5, 0, Item('wololo'))

    import ipdb; ipdb.set_trace()  # breakpoint
    print(a < b)
    print(a < c)  # A vem primeiro entao A é menor que B mesmo
                  # que a prioridade seja igual
    print(b < a)
    print(d < a)

    queue = PriorityQueue()
    queue.push(Item('foo'), 1)
    queue.push(Item('bar'), 5)
    queue.push(Item('spam'), 4)
    queue.push(Item('grok'), 1)
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
