import turtle


def square_drawer(my_turtle, a, distance, x=0, y=0, number_of_squares=1):
    if number_of_squares > 0:
        my_turtle.pu()
        my_turtle.setx(x)
        my_turtle.sety(y)
        my_turtle.pd()
        for i in range(4):
            my_turtle.forward(a)
            my_turtle.right(90)
        square_drawer(my_turtle, a + distance * 2, distance, x - distance, y + distance, number_of_squares - 1)


def main():
    my_turtle = turtle.Turtle()
    square_drawer(my_turtle, 10, 5, number_of_squares=50)


if __name__ == "__main__":
    main()
