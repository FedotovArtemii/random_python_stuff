import turtle


def main():
    my_turtle = turtle.Turtle()
    i = 0
    while True:
        my_turtle.left(30)
        my_turtle.forward(1/5 * i)
        i += 1


if __name__ == '__main__':
    main()
