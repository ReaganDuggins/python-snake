import Directions

directions = Directions.Directions()

class Player:
    def __init__(self, cell_size):
        self.position = {
            'x': -1,
            'y': -1
        }
        self.forward = directions.EAST
        self.segments = [{'x': -1, 'y': -1},{'x': -1, 'y': -1},{'x': -1, 'y': -1}]
        self.cell_size = cell_size
        self.self_destruct = False

    def change_direction(self, new_dir):
        dir = directions.from_ascii(new_dir)
        if(not directions.opposites(dir, self.forward) and
        dir is not None):
            self.forward = dir

    def add_segment(self, x, y):
        self.segments.insert(0,{
            'x': x,
            'y': y
        })

    def move(self):
        oldx = self.position['x']
        oldy = self.position['y']

        if(self.forward == directions.NORTH):
            self.position['y'] = self.position['y'] - self.cell_size
        if(self.forward == directions.WEST):
            self.position['x'] = self.position['x'] - self.cell_size
        if(self.forward == directions.SOUTH):
            self.position['y'] = self.position['y'] + self.cell_size
        if(self.forward == directions.EAST):
            self.position['x'] = self.position['x'] + self.cell_size
        
        for seg in self.segments:
            if self.position['x'] == seg['x'] and self.position['y'] == seg['y']:
                self.self_destruct = True

        if len(self.segments) > 0:
            self.segments.pop()
            self.add_segment(oldx, oldy)
        

    