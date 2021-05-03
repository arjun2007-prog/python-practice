# import colorgram
import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.hideturtle()
timmy.speed(0)
screen = Screen()
color_use = [(187, 18, 44), (243, 231, 66), (196, 75, 32), (218, 66, 107), (17, 124, 173), (196, 175, 17), (108, 181, 209), (12, 142, 88), (12, 166, 214), (210, 152, 96), (187, 41, 61), (241, 231, 2), (23, 39, 76), (77, 174, 94), (36, 44, 112), (215, 69, 50), (218, 130, 155), (124, 185, 119), (235, 165, 183), (5, 58, 39), (146, 209, 220), (8, 95, 55), (4, 86, 111), (162, 29, 27), (234, 171, 164), (162, 212, 176)]

timmy.penup()
turtle.colormode(255)
timmy.goto(-200,-200)

for j in range(10):#1
 #This for loop keeps the count of the lines
  for i in range(10):
      #this for loops keeps the count of the dots it needs to draw in a line
     timmy.dot(20, random.choice(color_use))
     timmy.forward(50)

  y = timmy.pos()[1]+50
  timmy.goto(-200, y)

screen.exitonclick()


