import turtle
a = turtle.Turtle()
a.speed(0)
a.getscreen().bgcolor("black")
a.penup()
a.pendown()
a.color("orange")
def star(turtle, size):
    if size <= 10:
        return
    else:
        turtle.begin_fill()
        for _ in range(5):
            turtle.forward(size)
            star(turtle, size / 3)
            turtle.left(216)
        turtle.end_fill()
a.speed(25)
star(a, 360)

turtle.done()
