import turtle
import math
import random
screen = turtle.screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(1)
color = ["red", "blue", "lime",
 "yellow", "cyan", "magenta", "orange", "pink"]
 for i in range(120):
    t.penup()
    t.goto(0, 40)
    angle = i * (math.pi * 2) / 120
    x = 16 * (math.sin(angle) ** 3) *
15
    y = (13 * math.cos(4 * angle)) * 15
    c = random.choice(colors)
    t.color(c)
    t.pendown()
    t.goto(x, y)
    for _ in range(8):
        t.forword(6)
        t.backword(6)
        t.right(45)

turtle.done()
