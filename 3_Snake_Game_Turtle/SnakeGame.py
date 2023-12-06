import turtle
import time
import random

delay = 0.1

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600,height=600)
wn.tracer(0)


snake_body = []


## snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "Right"


## shanke food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)


def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)

    elif head.direction == "down":
        y = head.ycor()
        head.sety(y-20)

    elif head.direction == "left":
        x = head.xcor()
        head.setx(x-20)

    elif head.direction == "right":
        x = head.xcor()
        head.setx(x+20)


wn.listen()
wn.onkey(go_up,"w")
wn.onkey(go_down,"s")
wn.onkey(go_left,"a")
wn.onkey(go_right,"d")


while True:
    wn.update()

    ## check for collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "right"
        
        ## just throw each element out 
        ## of the window
        for bodyelement in snake_body:
            bodyelement.goto(1000,1000)
        
        #snake_body = []

    if head.distance(food) < 20 :
        x = random.randint(-270,270)
        y = random.randint(-270,270)
        food.goto(x,y)
        new_body_part = turtle.Turtle()
        new_body_part.speed(0)
        new_body_part.shape("square")
        new_body_part.color("grey")
        new_body_part.penup()
        snake_body.append(new_body_part)
        #print(snake_body)

    ## the third item will follow second item
    ## the fourth item folow the third item
    ## and so on
    for item in range(len(snake_body)-1,0,-1):
        
        ## we loop through from the last
        ## and every element will follow
        ## their front element
        x = snake_body[item-1].xcor()
        y = snake_body[item-1].ycor()
        snake_body[item].goto(x,y)

    ## in this code i attach one more thing
    ## is that the second item follow the head
    ## and that will 

    if len(snake_body)>0:
        x = head.xcor()
        y = head.ycor()
        snake_body[0].goto(x,y)

    
    move()
    
    ##  collision with the head with the body
    ##  and collision means distance < 20
    ##  you have to leave the first segment
    ##  because its distance is already 20
    ##  so we do not consider the first first element
    ## thats why we start for 1 and not 0
    for item in range(1,len(snake_body)-1):
        if head.distance(snake_body[item]) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "Right"

            ## throw the element 
            ## of the snake body 
            ## out of the frame
            for bodyelem in snake_body:
                bodyelem.goto(1000,1000)
            snake_body = []
    
    time.sleep(delay)
    
