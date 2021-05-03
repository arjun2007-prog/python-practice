import turtle
from turtle import Turtle
import random

timmy = Turtle()
screen = turtle.Screen()


timmy.shape("turtle")

timmy.speed(0)
timmy.pensize(15)

directions = [0, 90, 180, 270]

for i in range(200):
    timmy.forward(50)
    timmy.setheading(random.choice(directions))

    R = random.random()
    B = random.random()
    G = random.random()
    color = (R, G, B)
    timmy.pencolor(color)

screen.exitonclick()


