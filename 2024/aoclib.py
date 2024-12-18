class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"({self.x},{self.y})"
    
    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)
    
    def __ne__(self,other):
        return not (self == other)

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        return Vector2(self.x * other, self.y * other)
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def magnitude(self):
        return (self.x**2 + self.y**2)**(1/2)
    

class Queue:
    def __init__(self,initial=[]):
        if not isinstance(initial, list): self.queue = [initial]
        else: self.queue = initial
    
    def __repr__(self):
        return "<"+', '.join(map(str, self.queue))+">"

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)
    
    def is_empty(self):
        return len(self.queue) == 0