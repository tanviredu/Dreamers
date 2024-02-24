import turtle

# Function to draw a triangle
def draw_triangle():
    for _ in range(3):
        turtle.forward(100)
        turtle.right(120)

# Function to draw a star
def draw_star():
    for _ in range(5):
        turtle.forward(100)
        turtle.right(144)

# Function to draw a pentagon
def draw_pentagon():
    for _ in range(5):
        turtle.forward(100)
        turtle.right(72)

# Function to draw a hexagon
def draw_hexagon():
    for _ in range(6):
        turtle.forward(100)
        turtle.right(60)


import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle
my_turtle = turtle.Turtle()
my_turtle.speed(0)  # Set the fastest drawing speed

# Define colors
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Function to draw a colorful spiral
def draw_spiral():
    for i in range(360):
        my_turtle.color(random.choice(colors))
        my_turtle.forward(i)
        my_turtle.left(121)

draw_spiral()

# Hide the turtle
my_turtle.hideturtle()