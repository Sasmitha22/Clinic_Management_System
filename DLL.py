class DoublyLinkedList:
    cap = 10
    class _Node:

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next
        
    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._size = 0
        self._header._next = self._trailer
        self._trailer._prev = self._header

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def is_full(self):
        return self._size == DoublyLinkedList.cap
        
    def _insert_btn(self, e, pred, succ):
        new = self._Node(e, pred, succ)
        pred._next = new
        succ._prev = new
        self._size += 1
        return new
    
    def _delete_node(self, node):
        pred = node._prev
        succ = node._next
        el = node._element
        pred._next = succ
        succ._prev = pred
        node._prev = node._element = node._next = None
        return el