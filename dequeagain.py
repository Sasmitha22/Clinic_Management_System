#deque
from DLL import DoublyLinkedList
class Deque(DoublyLinkedList):
    def __init__(self):
        super().__init__()
        self._pointer1 = self._header
        self._pointer2 = self._trailer
        self._count = 0
        self._first = 0
        self._last = 0
    def first(self):
        if self.is_empty():
            raise Empty('Queue Empty')
        return self._header._next._element
    
    def last(self):
        if self.is_empty():
            raise Empty('Queue Empty')
        return self._trailer._prev._element
    
    def insert_first(self, e):
        if self._first < 1:
            self._pointer1 = self._insert_btn(e, self._header, self._pointer2)
        else:
            self._pointer1 = self._insert_btn(e, self._pointer1, self._pointer2)
        self._count += 1
        self._first += 1

    def insert_last(self, e):
        if self._last < 1:
            self._pointer2 = self._insert_btn(e, self._trailer._prev, self._trailer)
        else:
            self._insert_btn(e, self._trailer._prev, self._trailer)
       
        self._count += 1
        self._last += 1

    def delete_first(self):
        if self.is_empty():
            raise Empty('Queue is Empty')
        self._delete_node(self._header._next)
        self._count -= 1

    def delete_last(self):
        if self.is_empty():
            raise Empty('Queue is Empty')
        self._delete_node(self._trailer._prev)
        self._count -= 1
    
    def __str__(self):
        app = []
        val = self._header._next
        while val._next is not None:
            app.append(val._element)
            val = val._next
        return app