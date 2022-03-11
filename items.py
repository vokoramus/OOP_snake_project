from navigator import *


class Figure:
    def __init__(self):
        self.p_list = []

    def draw(self):
        for pt in self.p_list:
            pt.draw()


class HorizontalLine(Figure):

    def __init__(self, x_left, x_right, y, sym):
        super().__init__()
        for x in range(x_left, x_right + 1):
            pt = Point(x, y, sym)
            self.p_list.append(pt)


class VerticalLine(Figure):
    def __init__(self, y_up, y_down, x, sym):
        super().__init__()
        self.p_list = []
        for y in range(y_up, y_down + 1):
            pt = Point(x, y, sym)
            self.p_list.append(pt)


class Point:
    def __init__(self, x=0, y=0, sym=''):
        self.x = x
        self.y = y
        self.sym = sym

    # def move(self, dx, dy):
    #     self.reset()
    #     self.x += dx
    #     self.y += dy
    #     self.draw()

    def move(self, offset, direction):
        if direction == 'right':
            self.x += offset
        elif direction == 'left':
            self.x -= offset
        if direction == 'up':
            self.y -= offset
        elif direction == 'down':
            self.y += offset


    def reset(self):
        pass

    def draw(self):
        r = self.y
        c = self.x
        s = self.sym
        sys_draw(r, c, s)


class Snake(Figure):
    def __init__(self, tail: Point, length, direction):
        super().__init__()
        for i in range(length):
            pt = Point(tail.x, tail.y, tail.sym)
            pt.move(i, direction)
            self.p_list.append(pt)
