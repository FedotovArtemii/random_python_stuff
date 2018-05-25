import turtle


def main():
    length = 10
    my_turtle = turtle.Turtle()
    for i in range(4):
        my_turtle.forward(length)
        my_turtle.left(90)


if __name__ == '__main__':
    main()
