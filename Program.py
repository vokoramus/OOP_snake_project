import os
from items import *


class Program:
    def Main(self):
        # print('Hello!')

        p1 = Point(10, 3, '*')
        p1.draw()

        p2 = Point(2, 2, '#')
        p2.draw()

        # line = HorizontalLine()
        line = HorizontalLine(5, 10, 8, '+')
        line.draw()

        line = VerticalLine(2, 6, 20, '.')
        line.draw()


if __name__ == '__main__':
    os.system('cls')
    p = Program()
    p.Main()

    while True:
        # i = input('Press Q to Quit or any other key to continue: ')
        i = input('')

        if i.capitalize() == 'Q':
            break
