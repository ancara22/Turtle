from turtle import Turtle, Screen
#from data import colors_data
import random
import colorgram


little_turtle = Turtle()
window = Screen()
window.colormode(255)


little_turtle.hideturtle()
little_turtle.color("white", "red")
little_turtle.speed(200)

colors = colorgram.extract('/Users/dinisbarcari/Desktop/100 python/Proj 10 (turtle 2)/iamge.jpg', 30)

def draw_a_line(step, start_X, start_Y):
	little_turtle.setpos(start_X, start_Y)
	i = 0
	while i != 25:
		color = random.choice(colors)
		little_turtle.color("white", (color.rgb.r, color.rgb.g, color.rgb.b))
		little_turtle.forward(step)
		little_turtle.begin_fill()
		little_turtle.circle(10)
		little_turtle.end_fill()
		i += 1




def draw_multiline():
	start_y = -290
	start_x = -330

	finish_x = 320

	for _ in range(0, 12):
		draw_a_line(25, start_x, start_y)
		start_y += 25
		draw_a_line(-25, finish_x, start_y)
		start_y += 25







draw_multiline()

window.exitonclick()


