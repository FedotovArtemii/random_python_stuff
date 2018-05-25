import turtle


def main():
    my_turtle = turtle.Turtle()
    i = 0
    while True:
        i += 1
        my_turtle.left(90)
        my_turtle.forward(5 * i)


if __name__ == '__main__':
    main()
