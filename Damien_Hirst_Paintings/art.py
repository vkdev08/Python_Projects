import turtle
import math
import random

# Setup screen
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.penup()
t.hideturtle()

# Constants
num_dots = 800
angle = 137.5  # Golden angle
c = 6          # Controls spacing
dot_size = 8

# Draw dots in spiral
for n in range(num_dots):
    theta = math.radians(n * angle)
    r = c * math.sqrt(n)

    x = r * math.cos(theta)
    y = r * math.sin(theta)

    t.goto(x, y)
    t.dot(dot_size, (
        random.random(),  # R
        random.random(),  # G
        random.random()   # B
    ))

turtle.done()
import turtle
import math
import random

# Setup
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.penup()
turtle.bgcolor("white")

# Constants
rings = 20            # Number of concentric circles
spacing = 15          # Distance between rings
dot_size = 8

# Loop over each ring
for r in range(1, rings + 1):
    radius = r * spacing
    dots_in_ring = 6 * r  # Number of dots increases per ring
    angle_step = 360 / dots_in_ring

    for i in range(dots_in_ring):
        theta = math.radians(i * angle_step)
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)

        t.goto(x, y)
        t.dot(dot_size, (
            random.random(),  # R
            random.random(),  # G
            random.random()   # B
        ))

turtle.done()
