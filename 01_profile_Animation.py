import turtle


screen = turtle.Screen()
screen.title("Simple Animation")
screen.bgcolor("white")


circle_turtle = turtle.Turtle()
circle_turtle.shape("circle")
circle_turtle.color("blue")


circle_turtle.penup()
circle_turtle.goto(-200, 0)


def move_circle():
    for _ in range(400):
        circle_turtle.forward(1)
        screen.update()

screen.tracer(0)


move_circle()


screen.exitonclick()
