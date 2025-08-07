import turtle

#screen
screen = turtle.Screen()
screen.colormode(255)

#turtle
timmy = turtle.Turtle()
timmy.speed("fastest")
radius = 2
spacing = 2
y = spacing
timmy.hideturtle()
for i in range(1,101):
    timmy.pendown()
    timmy.circle(radius)
    timmy.penup()
    timmy.goto(0,-i*spacing)
    radius += spacing
screen.exitonclick()