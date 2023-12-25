from turtle import *

color("white")

fillcolor("maroon")
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

color("white")
fillcolor("white")
begin_fill()
for item in range(2):
  forward(30)
  left(90)
  forward(100)
  left(90)
end_fill()


penup()
goto(0,50)
pendown()

fillcolor("white")
begin_fill()
for item in range(2):
  forward(200)
  left(90)
  forward(30)
  left(90)
end_fill()




penup()
goto(50,0)
pendown()

color("blue")
fillcolor("dark blue")
begin_fill()
for item in range(2):
  forward(10)
  left(90)
  forward(100)
  left(90)
end_fill()




penup()
goto(0,60)
pendown()

fillcolor("dark blue")
begin_fill()
for item in range(2):
  forward(200)
  left(90)
  forward(10)
  left(90)
end_fill()