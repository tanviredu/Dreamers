from turtle import *
penup()
goto(-150,0)
pendown()

fillcolor("blue")
begin_fill()
for _ in range(2):
    forward(300)
    left(90)
    forward(200)
    left(90)
end_fill()



## the white cross
penup()
goto(-150,80)
pendown()

fillcolor("white")
begin_fill()
for _ in range(2):
    forward(300)
    left(90)
    forward(40)
    left(90)
end_fill()


penup()
goto(-150+64,200)
pendown()
fillcolor("white")
begin_fill()
for _ in range(2):
    forward(40)
    right(90)
    forward(200)
    right(90)
end_fill()

penup()
goto(-150,90)
pendown()
fillcolor("red")
begin_fill()
for _ in range(2):
    forward(300)
    left(90)
    forward(20)
    left(90)
end_fill()


penup()
goto(-150+74,200)
pendown()
fillcolor("red")
begin_fill()
for _ in range(2):
    forward(20)
    right(90)
    forward(200)
    right(90)
end_fill()