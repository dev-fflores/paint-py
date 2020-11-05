class Vector:
    x = 0.0
    y = 0.0
    
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
        
    def __add__(self, vector):
        return Vector(self.x + vector.x, self.y + vector.y)
    
    def __sub__(self, vector):
        return Vector(self.x - vector.x, self.y - vector.y)
        
    def __str__(self):
        return "["+str(self.x)+","+str(self.y)+"]"
