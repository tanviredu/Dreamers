from turtle import *

## we draw 4 circle in 4 different 
## subco ordinatie
speed(2)
penup()
goto(50,50)
pendown()
begin_fill()
fillcolor("red")
circle(20)
end_fill()

penup()
goto(-50,50)
pendown()
begin_fill()
fillcolor("red")
circle(20)
end_fill()

penup()
goto(-50,-50)
pendown()
begin_fill()
fillcolor("red")
circle(20)
end_fill()

penup()
goto(50,-50)
pendown()
begin_fill()
fillcolor("red")
circle(20)
end_fill()

done()
