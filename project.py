import turtle
turtle.Screen().bgcolor("green")
turtle.Screen().setup(300,400)
pen = turtle.Turtle()

sides = 4
sideLength = 100
angle = 360/sides
for i in  range(sides):
    pen.forward(sideLength)
    pen.right(angle)

turtle.done()