from turtle import *

color("white")

fillcolor("white")
begin_fill()
for item in range(2):
  forward(200)
  left(90)
  forward(100)
  left(90)
end_fill()

penup()
goto(40,0)
pendown()

color("blue")
fillcolor("blue")
begin_fill()
for item in range(2):
  forward(20)
  left(90)
  forward(100)
  left(90)
end_fill()

penup()
goto(0,50)
pendown()

fillcolor("blue")
begin_fill()
for item in range(2):
  forward(200)
  left(90)
  forward(20)
  left(90)
end_fill()