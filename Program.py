import os
from items import *
from time import sleep
from keys import keyboard_listener


class Program:
    def main(self):

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
        p1 = Point(1, 1, '*')
        p1.draw()

        snake = Snake(p1, 4, 'right')
        snake.draw()

        # еда
        food_creator = FoodCreator(78, 24, '$')  # габариты экрана
        food = food_creator.create_food()
        food.draw()

        while True:

            if snake.eat(food):
                print('!', end='')
                food = food_creator.create_food()
                food.draw()
            else:
                snake.move()

            key = keyboard_listener()
            if key == 'Esc':
                break

            sleep(0.1)
            snake.handle_key(key)



if __name__ == '__main__':
    os.system('cls')
    # os.system('mode 82, 26')
    p = Program()
    p.main()
