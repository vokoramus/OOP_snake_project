import os
from items import *
from time import sleep
from keys import keyboard_listener


class Program:
    def main(self):

        v1 = VerticalLine(0, 5, 25, '|')
        h1 = HorizontalLine(0, 8, 10, '-')

        lines = []
        lines.append(v1)
        lines.append(h1)

        pt = Point(4, 5, '*')
        f_snake = Snake(pt, 15, 'right')

        snake = f_snake

        figures = []
        figures.append(f_snake)
        figures.append(v1)
        figures.append(h1)

        for f in figures:
            self.draw(f)

        # рамка
        walls = Walls(78, 24)
        walls.draw()

        # еда
        food_creator = FoodCreator(78, 24, '$')  # габариты экрана
        food = food_creator.create_food()
        food.draw()

        while True:
            stop = False
            for line in lines:
                if line.is_hit(snake):
                    stop = True
            if stop:
                break


            if walls.is_hit(snake) or snake.is_hit_tail():
                break

            if snake.eat(food):
                food = food_creator.create_food()
                food.draw()
            else:
                snake.move()

            key = keyboard_listener()
            if key == 'Esc':
                break

            sleep(0.1)
            snake.handle_key(key)

    def draw(self, figure):
        figure.draw()


if __name__ == '__main__':
    os.system('cls')
    # os.system('mode 82, 26')
    p = Program()
    p.main()
