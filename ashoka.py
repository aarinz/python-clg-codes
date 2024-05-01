import turtle
t = turtle.Turtle()

t.pencolor("navy")
t.circle(50)
for _ in range(24):

    t.goto(0,50)
    t.forward(50)
    t.backward(50)
    t.right(360/24)