# black red gold

from turtle import *
bgcolor("white")

penup()
goto(-150,60)
pendown()
fillcolor("black")
begin_fill()
for _ in range(2):
    forward(300)
    right(90)
    forward(40)
    right(90)
end_fill()

penup()
goto(-150,20)
pendown()
fillcolor("red")
begin_fill()
for _ in range(2):
    forward(300)
    right(90)
    forward(40)
    right(90)
end_fill()


penup()
goto(-150,-20)
pendown()
fillcolor("gold")
begin_fill()
for _ in range(2):
    forward(300)
    right(90)
    forward(40)
    right(90)
end_fill()

hideturtle()
done()


