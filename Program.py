# from navigator import *
import os
from ctypes import *
from time import sleep

STD_OUTPUT_HANDLE = -11

class COORD(Structure):
    pass

COORD._fields_ = [("X", c_short), ("Y", c_short)]


class Program:
    def Main(self):
        # print('Hello!')

        p1 = Point(1, 3, '*')
        p1.draw()

        p2 = Point(2, 2, '#')
        p2.draw()

        list_1 = [p1, p2]

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
        r = self.x
        c = self.y
        s = self.sym

        h = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
        windll.kernel32.SetConsoleCursorPosition(h, COORD(c, r))

        c = s.encode("windows-1252")
        windll.kernel32.WriteConsoleA(h, c_char_p(c), len(c), None, None)


if __name__ == '__main__':
    os.system('cls')
    p = Program()
    p.Main()

    # print_at(2, 4, "Hello")

    while True:
        # i = input('Press Q to Quit or any other key to continue: ')
        i = input('')

        if i.capitalize() == 'Q':
            break
