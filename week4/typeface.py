import turtle

turtle.setup(800,800)

logo = turtle.Turtle()
logo.pencolor("blue")
logo.speed(10)

logo.up()
logo.setpos(-375,375)

for i in range(4):
    logo.down()
    logo.dot(5,"blue")
    logo.forward(50)
    logo.right(90)

logo.up()
logo.setpos(logo.pos() + (125,-50))
logo.right(180)

logo.down()
logo.dot(5,"blue")
logo.forward(50)
logo.dot(5,"blue")
logo.right(120)
logo.forward(55)
logo.dot(5,"blue")
logo.right(120)
logo.forward(35)
logo.dot(5,"blue")
logo.right(120)
logo.forward(25)
logo.dot(5,"blue")

logo.up()
logo.setpos(logo.pos() + (55,-15))
logo.right(180)

logo.down()
logo.dot(5,"blue")
logo.right(270)
logo.forward(50)
logo.dot(5,"blue")
logo.right(110)
logo.forward(35)
logo.dot(5,"blue")
logo.right(130)
logo.forward(35)
logo.dot(5,"blue")
logo.right(230)
logo.forward(35)
logo.dot(5,"blue")
logo.right(145)
logo.forward(35)
logo.dot(5,"blue")

logo.up()
logo.setpos(logo.pos() + (95,0))
logo.right(180)


turtle.exitonclick()
