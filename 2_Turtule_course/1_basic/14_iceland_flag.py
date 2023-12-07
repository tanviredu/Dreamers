from turtle import *
bgcolor("white")
speed(2)


## the background flag
penup()
goto(0,0)
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
goto(0,80)
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
goto(64,200)
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
goto(0,90)
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
goto(74,200)
pendown()
fillcolor("red")
begin_fill()
for _ in range(2):
    forward(20)
    right(90)
    forward(200)
    right(90)
end_fill()


done()
