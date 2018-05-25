import turtle


def main():
    n = 120
    my_turtle = turtle.Turtle()
    for i in range(n):
        my_turtle.forward(120)
        my_turtle.stamp()
        my_turtle.left(180)
        my_turtle.forward(120)
        my_turtle.left(180 + 360 / n)


if __name__ == '__main__':
    main()
