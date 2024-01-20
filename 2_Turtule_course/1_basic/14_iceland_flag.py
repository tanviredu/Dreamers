from turtle import *

penup()
goto(-150,0)
pendown()

fillcolor("midnight blue")
begin_fill()
for item in range(2):
  forward(300)
  left(90)
  forward(200)
  left(90)
end_fill()

penup()
goto(-150,80)
pendown()
color("white")
fillcolor("white")
begin_fill()
for item in range(2):
  forward(300)
  left(90)
  forward(40)
  left(90)
end_fill()


penup()
goto(-86,200)
pendown()
color("white'")
fillcolor("white")
begin_fill()
for item in range(2):
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
for item in range(2):
  forward(300)
  left(90)
  forward(20)
  left(90)
end_fill()

penup()
goto(-76,200)
pendown()

color("red")
fillcolor("red")
begin_fill()
for item in range(2):
  forward(20)
  right(90)
  forward(200)
  right(90)
end_fill()

hideturtle()
