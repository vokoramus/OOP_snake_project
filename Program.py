import os
from items import *


class Program:
    def Main(self):

        # рамка
        line_high = HorizontalLine(0, 78, 0, '+')
        line_bottom = HorizontalLine(0, 78, 24, '+')
        line_left = VerticalLine(0, 24, 0, '+')
        line_right = VerticalLine(0, 24, 78, '+')

        line_high.draw()
        line_bottom.draw()
        line_left.draw()
        line_right.draw()

        # точки
        p1 = Point(10, 3, '*')
        p1.draw()

        snake = Snake(p1, 4, 'right')
        snake.draw()

if __name__ == '__main__':
    os.system('cls')
    # os.system('mode 82, 26')
    p = Program()
    p.Main()

    while True:
        # i = input('Press Q to Quit or any other key to continue: ')
        i = input('')

        if i.capitalize() == 'Q':
            break
