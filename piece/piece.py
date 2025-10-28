from tools.rotation_utils import rotate_positions

class Piece:
    def __init__(self, x_positions, y_positions, center_x, center_y):
        self.center_x = center_x
        self.center_y = center_y
        self.x_positions = x_positions
        self.y_positions = y_positions

    def get_positions(self):
        return list(zip(self.x_positions,self.y_positions))

    def move(self, direction="down"):
        if(direction=="right"):
            self.x_positions = [x+1 for x in self.x_positions]
            self.center_x += 1
        elif(direction=="left"):
            self.x_positions = [x-1 for x in self.x_positions]
            self.center_x -= 1
        elif(direction=="down"):
            self.y_positions = [x-1 for x in self.y_positions]
            self.center_y -= 1

    def get_needed_rotation_space(self):
        # for board to check if there is enough room for a rotation to be performed. If there is not enough space, then movements to the sides will be performed. In some tetris versions when the piece is near the bottom and a rotation makes the piece go up, it allows it, but for this version we will not support this feature, we simply wont allow a rotation if there is not enough space for it below.
        radius = 0
        for i in range(len(self.x_positions)):
            x_variation = abs(self.center_x - self.x_positions[i])
            y_variation = abs(self.center_y - self.y_positions[i])
            if(x_variation>radius):
                radius = x_variation
            if(y_variation>radius):
                radius = y_variation
        x_extremes = [self.center_x-radius,self.center_x+radius]
        y_extremes = [self.center_y-radius,self.center_y+radius]
        return [x_extremes,y_extremes]

    def rotate(self, rotations = 1):
        # with this we provide the possible
        new_positions = rotate_positions(self.get_positions(), (self.center_x,self.center_y), rotations)

        xs, ys = zip(*new_positions)
        self.x_positions = list(xs)
        self.y_positions = list(ys)

