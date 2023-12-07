from turtle import *
bgcolor("yellow")
begin_fill()
penup()
goto(-150,60)
pendown()
fillcolor("red")
for _ in range(2):
    forward(300)
    right(90)
    forward(40)
    right(90)
end_fill()

penup()
goto(-150,20)
pendown()
fillcolor("white")
begin_fill()
for _ in range(2):
    forward(300)
    right(90)
    forward(40)
    right(90)
end_fill()

done()