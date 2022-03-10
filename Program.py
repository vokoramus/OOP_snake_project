from navigator import *
import os

class Program:
    def Main(self):
        # print('Hello!')
        x1 = 1
        y1 = 3
        sym1 = '*'
        draw(x1, y1, sym1)

        x2 = 2
        y2 = 2
        sym2 = '#'
        draw(x2, y2, sym2)


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