#Pqueue

class PQueue:
    def_cap = 10
    def __init__(self):
        self._arr = [None] * PQueue.def_cap
        self._high = self._arr[:PQueue.def_cap//2]
        self._low = self._arr[PQueue.def_cap//2:]
        self._highsize = 0
        self._lowsize = 0
        self._fronth = 0
        self._frontl = 0
        self._front = 0
        self._arrsize = len(self._arr)
        self._deqcount = 0
    
    def __len__(self, n):
        if n == 0:
            return self._highsize
        elif n == 1:
            return self._lowsize
        else:
            return "Invalid queue"
    
    def first(self, n):
        if self.is_empty(0) and n == 0:
            raise Empty("Queue is empty")
        elif self.is_empty(1) and n == 1:
            raise Empty('Queue is empty')
        elif n == 0 and self.is_empty(0) == False:
            return self._high[self._fronth]
        elif n == 1 and self.is_empty(1) == False:
            return self._low[self._frontl]
        else:
            raise Exception('Invalid queue')
    
    def is_empty(self, n):
        if n == 0:
            return self._highsize == 0
        elif n == 1:
            return self._lowsize == 0
        else:
            return "Invalid Queue"
    
    def enqueue(self, p, el,):
        if p == 0:

            if self._highsize == len(self._high):
                self._resize(2 * self._arrsize)
                self._high = self._arr[:len(self._arr)//2]
                self._low = self._arr[len(self._arr)//2: len(self._arr)]
            avail = (self._fronth + self._highsize) % len(self._high)
            self._high[avail] = el
            self._highsize += 1
        elif p == 1:
            if self._lowsize == len(self._low):
                self._resize(2 * self._arrsize)
                self._high = self._arr[:len(self._arr)//2]
                self._low = self._arr[len(self._arr)//2: len(self._arr)]
            avail = (self._frontl + self._lowsize) % len(self._low)
            self._low[avail] = el
            self._lowsize += 1
        else:
            raise Exception("Priority does not exist")
    
    def dequeue(self):
        if self.is_empty(0):
            #pop from 1
            if self.is_empty(1):
                raise Empty('Both queue are empty')
            else:
                el = self._low[self._frontl]
                self._low[self._frontl] = None
                self._frontl = (self._frontl + 1) % len(self._low)
                self._lowsize -= 1
                return el
        else:
            el = self._high[self._fronth]
            self._high[self._fronth] = None
            self._fronth = (self._fronth + 1) % len(self._high)
            self._highsize -= 1
            return el
    
    def _resize(self, capacity):
        old_high = self._high + [None] * (self._arrsize - self._highsize)
        old_low = self._low + [None] * (self._arrsize - self._lowsize)
        new = [None] * capacity
        walk1 = self._fronth
        walk2 = self._frontl
        for i in range(capacity//2):
            new[i] = old_high[walk1]
            walk1 = (1+walk1)%len(old_high)
        for j in range(capacity//2, capacity):
            new[j] = old_low[walk2]
            walk2 = (1+walk2)%len(old_low)
        self._arr = new
        self._front = 0
    
    def __str__(self, n):
        if n == 0:
            print("High Priority Queue:")
            for i in self._high[:-1]:
                print(i)
            return self._high[-1]
        elif n == 1:
            print("Low Priority Queue:")
            for i in self._low[:-1]:
                print(i)
            return self._low[-1]
        else:
            print("Queue Invalid")
    
            
