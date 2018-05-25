import turtle


def draw(my_turtle, number_of_angles, len_of_side):
    angle = 365 / number_of_angles
    for i in range(number_of_angles):
        my_turtle.forward(len_of_side)
        my_turtle.left(angle)


def main():
    n = int(input('please insert number of angles'))
    length = int(input('please insert length'))
    my_turtle = turtle.Turtle()
    draw(my_turtle, n, length)


if __name__ == '__main__':
    main()
