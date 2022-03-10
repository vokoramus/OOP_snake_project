from navigator import *

class HorizontalLine():
    # def __init__():
    #     self.p_list = []
        # p1 = Point(4, 4, '*')
        # p2 = Point(4, 5, '*')
        # p3 = Point(4, 6, '*')
        # self.p_list.append(p1)
        # self.p_list.append(p2)
        # self.p_list.append(p3)

    def __init__(self, x_left, x_right, y, sym):
        self.p_list = []
        for x in range(x_left, x_right + 1):
            pt = Point(x, y, sym)
            self.p_list.append(pt)

    def draw(self):
        for pt in self.p_list:
            pt.draw()

class VerticalLine():
    def __init__(self, y_up, y_down, x, sym):
        self.p_list = []
        for y in range(y_up, y_down + 1):
            pt = Point(x, y, sym)
            self.p_list.append(pt)

    def draw(self):
        for pt in self.p_list:
            pt.draw()


class Point:
    def __init__(self, x=0, y=0, sym=''):
        self.x = x
        self.y = y
        self.sym = sym

    def move(self, dx, dy):
        self.reset()
        self.x += dx
        self.y += dy
        self.draw()

    def reset(self):
        pass

    def draw(self):
        r = self.y
        c = self.x
        s = self.sym
        sys_draw(r, c, s)
