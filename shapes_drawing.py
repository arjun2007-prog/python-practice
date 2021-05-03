import turtle
from turtle import Turtle
from random import random

timmy = Turtle()
screen = turtle.Screen()


timmy.shape("turtle")

timmy.speed(2)
sides_of_shape = 3
timmy.pensize(10)

def draw_shape(sides) :
  for i in range(sides) :
    timmy.forward(50)
    timmy.left(360/sides)
    timmy.forward(50)
  R = random()
  B = random()
  G = random()

  timmy.color(R, G, B)


for i in range(3,11):
  draw_shape(sides_of_shape)
  sides_of_shape += 1

screen.exitonclick()


