from turtle import *

penup()
pendown()
fillcolor("white")
begin_fill()
for item in range(2):
  forward(200)
  left(90)
  forward(50)
  left(90)
end_fill()

goto(0,-50)
fillcolor("green")
begin_fill()
for item in range(2):
  forward(200)
  left(90)
  forward(50)
  left(90)
end_fill()
goto(0,-100)
fillcolor("red")
begin_fill()
for item in range(2):
  forward(200)
  left(90)
  forward(50)
  left(90)
end_fill()