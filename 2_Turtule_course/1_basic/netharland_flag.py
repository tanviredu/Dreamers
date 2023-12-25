from turtle import *

color("white")

penup()
goto(-50,0)
pendown()
fillcolor("red")
begin_fill()
for item in range(2):
  forward(200)
  left(90)
  forward(50)
  left(90)
end_fill()

penup()
goto(-50,-50)
pendown()
fillcolor("white")
begin_fill()
for item in range(2):
  forward(200)
  left(90)
  forward(50)
  left(90)
end_fill()


penup()
goto(-50,-100)
pendown()
fillcolor("blue")
begin_fill()
for item in range(2):
  forward(200)
  left(90)
  forward(50)
  left(90)
end_fill()
