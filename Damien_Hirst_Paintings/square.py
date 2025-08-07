import turtle,colorgram,random

#variables
X,Y,spacing = -100,-100,20

#screen
screen = turtle.Screen()
screen.colormode(255)
#turtle
timmy = turtle.Turtle()
timmy.hideturtle()
timmy.penup()
#colors from img
colors = []
image = colorgram.extract("img.png",100)
for color in image:
      r = color.rgb.r
      g = color.rgb.g
      b = color.rgb.b
      colors.append((r,g,b))
print(colors)
timmy.goto(X,Y)
for _ in range(10):
      for _ in range(10):
            timmy.pendown()
            timmy.dot(10,random.choice(colors))
            timmy.penup()
            timmy.forward(spacing)
      Y = Y + spacing
      timmy.goto(X,Y)


screen.exitonclick()
