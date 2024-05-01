import turtle
t = turtle.Turtle()
t.hideturtle()

t.penup()
t.goto(-450,250)
t.pendown() 


t.fillcolor("orange")
t.begin_fill()
t.forward(300)
t.right(90)
t.forward(100)
t.right(90)
t.forward(300)
t.right(90)
t.forward(100)
t.end_fill()

t.left(180)


t.penup()
t.forward(300)
t.pendown()

t.fillcolor("green")
t.begin_fill()
t.left(90)
t.forward(300)
t.left(90)
t.forward(100)
t.left(90)
t.forward(300)
t.left(90)
t.forward(100)
t.end_fill()

t.left(90)


t.penup()
t.forward(200)
t.pendown()

t.left(90)

t.penup()
t.forward(150)
t.pendown()

t.fillcolor("navy")
t.begin_fill()
t.circle(50)
t.end_fill()

turtle.done()