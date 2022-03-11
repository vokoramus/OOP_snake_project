from navigator import *
from random import randint
import os


class Figure:
    def __init__(self):
        self.p_list = []

    def draw(self):
        for pt in self.p_list:
            pt.draw()

    def is_hit(self, figure):
        for pt in self.p_list:
            if figure.is_hit_point(pt):
                return True

        return False

    def is_hit_point(self, point):
        for pt in self.p_list:
            if pt.is_hit(point):
                return True

        return False


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

    def move(self, offset, direction):
        if direction == 'right':
            self.x += offset
        elif direction == 'left':
            self.x -= offset
        if direction == 'up':
            self.y -= offset
        elif direction == 'down':
            self.y += offset

    def clear(self):
        self.sym = ' '
        self.draw()

    def draw(self):
        r = self.y
        c = self.x
        s = self.sym
        sys_draw(r, c, s)

    def is_hit(self, p2):
        return self.x == p2.x and self.y == p2.y


class Snake(Figure):

    def __init__(self, tail: Point, length, direction):
        super().__init__()
        self.direction = direction
        for i in range(length):
            pt = Point(tail.x, tail.y, tail.sym)
            pt.move(i, self.direction)
            self.p_list.append(pt)
        self.keys_funcs = {
            'w': 'up',
            's': 'down',
            'a': 'left',
            'd': 'right',
        }

        self.keys_funcs_keys = self.keys_funcs.keys()

    def move(self):
        tail = self.p_list[0]
        self.p_list.remove(tail)
        head = self.get_next_point()
        self.p_list.append(head)

        tail.clear()
        head.draw()

    def get_next_point(self):
        head = self.p_list[-1]
        next_point = Point(head.x, head.y, head.sym)
        next_point.move(1, self.direction)
        return next_point

    def is_hit_tail(self):
        head = self.p_list[-1]
        for i in range(len(self.p_list) - 2):
            if head.is_hit(self.p_list[i]):
                return True
        return False

    def handle_key(self, key):
        if key in self.keys_funcs_keys:
            # print(keys_funcs[key])
            self.direction = (self.keys_funcs[key])

    def eat(self, food):
        head = self.get_next_point()
        if head.is_hit(food):
            food.sym = head.sym
            food.draw()
            self.p_list.append(food)
            return True
        else:
            return False

    # TODO: переопределить цвет и фон различных фигур
    def draw(self):
        # os.system('color 69')  # sets the background to blue
        super().draw()
        # os.system('color 96')  # sets the background to blue


class FoodCreator:
    def __init__(self, map_width, map_height, sym):
        self.map_width = map_width
        self.map_height = map_height
        self.sym = sym

    def create_food(self):
        x = randint(1, self.map_width - 1)
        y = randint(1, self.map_height - 1)

        return Point(x, y, self.sym)


class Walls(Figure):
    def __init__(self, map_width, map_height):
        super().__init__()
        self.wall_list = []

        up_line = HorizontalLine(0, map_width, 0, '+')
        down_line = HorizontalLine(0, map_width, map_height, '+')
        left_line = VerticalLine(0, map_height, 0, '+')
        right_line = VerticalLine(0, map_height, map_width, '+')

        self.wall_list.append(up_line)
        self.wall_list.append(down_line)
        self.wall_list.append(left_line)
        self.wall_list.append(right_line)

    def draw(self):
        for wall in self.wall_list:
            wall.draw()

    def is_hit(self, figure):
        for wall in self.wall_list:
            if wall.is_hit(figure):
                return True
