from turtle import *
bgcolor("white")

def part_of_flag(color,y_position):
    penup()
    goto(-150,y_position)
    pendown()
    fillcolor(color)
    begin_fill()
    for _ in range(2):
        forward(300)
        right(90)
        forward(40)
        right(90)
    end_fill()

part_of_flag("red",60)
part_of_flag("white",20)
part_of_flag("red",-20)
hideturtle()
done()

