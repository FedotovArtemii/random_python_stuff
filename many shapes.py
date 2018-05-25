import turtle
from math import sin, tan, radians


def builder(my_turtle, length, amount_of_shapes=1, counter=3):
    if counter < amount_of_shapes:
        angle = 360 / counter
        radius = length / 2 * sin(angle / 2)
        for i in range(counter):
            my_turtle.forward(2 * length)
            my_turtle.left(angle)
        builder(my_turtle, radius, amount_of_shapes, counter + 1)


def main():
    my_turtle = turtle.Turtle()
    builder(my_turtle, 80, 8)


if __name__ == '__main__':
    main()
