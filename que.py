class Deque:
    def __init__(self):
        self.stack = []

    def addFront(self, item):
        array = self.stack
        array.append(item)
        self.stack = array
    def addTail(self, item):
        ARRAY = [] # a - ARRAY
        ARRAY.append(item)
        ARRAY.append(self.stack)
        self.stack = ARRAY
    def removeFront(self):
        if len(self.stack) != 0:
            ARRAY = self.stack[len(self.stack)-1]
            del self.stack[len(self.stack)-1]
            return ARRAY
        else:
            return None # если очередь пуста
    def removeTail(self):
        # удаление из хвоста
        if len(self.stack) != 0:
            ARRAY = self.stack[0]
            del self.stack[0]
            return ARRAY
        else:
            return None # если очередь пуста
    def size(self):
        return len(self.stack) # размер очереди
deq = Deque()
deq.addFront("f1")
deq.addTail("t1")
deq.addFront("f2")
deq.addTail("t2")
while deq.size() > 0:
    print(deq.removeFront())
    print(deq.removeTail())
