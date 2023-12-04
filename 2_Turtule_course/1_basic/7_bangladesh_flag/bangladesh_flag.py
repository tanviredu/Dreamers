from turtle import *
speed(2)

## first we make the rectangle
## and the color will be green

begin_fill()
fillcolor("green")
forward(300)
right(90)
forward(200)
right(90)
forward(300)
right(90)
forward(200)
end_fill()

penup()
goto(150+50,-100)
pendown()
begin_fill()
fillcolor("red")
circle(50)
end_fill()

done()
