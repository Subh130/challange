import turtle #importing library

paper = turtle.Screen() #make the paper or the screen
paper.bgcolor("white") #Set the paper background color
paper.title("Turtle")

pen = turtle.Turtle()#make the pen
pen.color("Pink")
pen.fillcolor("red")
pen.begin_fill()
pen.left(120)
pen.forward(120)

for i in range (181):
    pen.right(1)
    pen.forward(1)

pen.left(90)

for i in range (181):
    pen.right(1)
    pen.forward(1)

pen.forward(150)
pen.end_fill()

turtle.done()