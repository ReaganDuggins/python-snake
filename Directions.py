class Directions:
    def __init__(self):
        self.NORTH = 'n'
        self.SOUTH = 's'
        self.EAST = 'e'
        self.WEST = 'w'

    def from_ascii(self, ascii):
        if ascii == 119:
            return self.NORTH
        if ascii == 97:
            return self.WEST
        if ascii == 115:
            return self.SOUTH
        if ascii == 100:
            return self.EAST
        
        
    def opposites(self, a, b):
        ns = [self.NORTH, self.SOUTH]
        ew = [self.EAST, self.WEST]
        return ((a in ns and
           b in ns) or
           (a in ew and
           b in ew))




