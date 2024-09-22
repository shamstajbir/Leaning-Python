import turtle
from turtle import *

# Setup the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Initialize turtle
pen = turtle.Turtle()
pen.speed(10)
pen.color("red")

# Function to draw a rose petal
def draw_petal():
    pen.begin_fill()
    pen.circle(100, 60)
    pen.left(120)
    pen.circle(100, 60)
    pen.left(120)
    pen.end_fill()

# Draw the rose flower
pen.penup()
pen.goto(0, -100)
pen.pendown()

# Drawing 6 petals
for i in range(6):
    draw_petal()
    pen.left(60)

# Draw the stem
pen.color("green")
pen.right(90)
pen.penup()
pen.forward(250)
pen.pendown()
pen.forward(300)

# Hide the turtle and finish
pen.hideturtle()
turtle.done()
