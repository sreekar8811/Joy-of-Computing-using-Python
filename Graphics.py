#-*- coding: utf-8 -*-
"""
Created on Tue Mar 26 17:20:29 2024
@author: sreekar
"""


from random import randint
import turtle

# Set up the turtle window
turtle.bgcolor("black")  # Changed "color" to "black" for better visibility
tur = turtle.Turtle()
tur.speed(0)  # Set the fastest drawing speed

# Define drawing parameters
dot_distance = 25
width = 5
height = 7

# Set up color list
list_color = ["white", "yellow", "brown", "red", "blue", "green", "orange"]

# Position the turtle
tur.penup()
tur.setpos(-250, 250)

def spiral(m, n):
    k = 0
    l = 0
    f = 0
    
    while (k < m and l < n):
        # Choose a random color
        col = randint(0, len(list_color) - 1)
        tur.color(list_color[col])
        
        if (f == 1):
            tur.right(90)
        
        # Draw the top row
        for i in range(l, n):
            tur.dot()
            tur.forward(dot_distance)
        k += 1
        f = 1
        
        tur.right(90)
        
        # Draw the right column
        if (k < m):
            for i in range(k, m):
                tur.dot()
                tur.forward(dot_distance)
            n -= 1
        
        tur.right(90)
        
        # Draw the bottom row
        if (l < n):
            for i in range(n - 1, l - 1, -1):
                tur.dot()
                tur.forward(dot_distance)
            m -= 1
        
        tur.right(90)
        
        # Draw the left column
        if (k < m):
            for i in range(m - 1, k - 1, -1):
                tur.dot()
                tur.forward(dot_distance)
            l += 1

# Set the size of the spiral
r = 20
c = 20

# Draw the spiral
spiral(r, c)

# Keep the window open
turtle.done()
