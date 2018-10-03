import turtle

# Typographic Properties as Global Variables
capHeight = 50


def setup():
    turtle.up()
    turtle.setup(800,800)
    turtle.pencolor("blue")
    turtle.speed(5)
    turtle.setpos(-375,375)


def kerning():
    turtle.up()
    turtle.setpos(turtle.pos() + (125,-50))
    turtle.right(180)

def square():
    global capHeight
    for i in range(4):
        turtle.down()
        turtle.dot(5,"blue")
        turtle.forward(capHeight)
        turtle.right(90)
    kerning()

def character():
    kerning()
    for i in range(4):
        turtle.down()
        logo.dot(5,"blue")
        logo.forward()

def main():
    setup()
    square()
    turtle.exitonclick()

main()
