from turtle import Turtle, Screen
from data import colors_data
from random import *

window = Screen()
turtle = Turtle()

turtle.speed(10)
turtle.hideturtle()
turtle.pensize(10)
window.colormode(255)


direction = [0, 90, 270, 180]

for _ in range(0, 200):

	r = randint(0, 255)
	g = randint(0, 255)
	b = randint(0, 255)
	turtle.pencolor(r, g, b)
	turtle.left(choice(direction))
	turtle.forward(20)




window.exitonclick()