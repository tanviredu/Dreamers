from turtle import *

penup()
goto(-50,0)
pendown()
fillcolor("black")
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
fillcolor("red")
begin_fill()
for item in range(2):
  forward(200)
  left(90)
  forward(50)
  left(90)
end_fill()

penup()
goto(50,-23)
pendown()
fillcolor("yellow")
begin_fill()
circle(20)
end_fill()