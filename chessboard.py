import turtle

t = turtle.Turtle()

t.hideturtle()
t.speed(0)

for i in range(8):
    for j in range(8):
        t.penup()
        t.goto(j*50, i*50)
        t.pendown()

        if (i+j) % 2 == 0:
             t.fillcolor("white")
        else:
            t.fillcolor("black")

        t.begin_fill()
        for _ in range(4):
            t.forward(50)
            t.left(90)
        t.end_fill()
turtle.done()
