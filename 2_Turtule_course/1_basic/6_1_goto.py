from turtle import *

## we draw 4 circle in 4 different 
## subco ordinatie
speed(2)
penup()
goto(150,150)
pendown()
begin_fill()
fillcolor("red")
circle(50)
end_fill()

penup()
goto(-150,150)
pendown()
begin_fill()
fillcolor("red")
circle(50)
end_fill()

penup()
goto(-150,-150)
pendown()
begin_fill()
fillcolor("red")
circle(50)
end_fill()

penup()
goto(150,-150)
pendown()
begin_fill()
fillcolor("red")
circle(50)
end_fill()

done()
