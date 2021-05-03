import turtle
from turtle import Turtle
from random import random

timmy = Turtle()
screen = turtle.Screen()

timmy.speed(0)
timmy.width(2)

def change_color() :
    R = random()
    B = random()
    G = random()

    timmy.color(R, G, B)


for i in range(72):
 timmy.circle(100)
 timmy.right(5)
 change_color()

screen.exitonclick()
