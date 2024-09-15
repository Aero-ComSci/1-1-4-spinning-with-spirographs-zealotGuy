import turtle

# Set up the turtle
turtle.setup(800, 800)
turtle.speed(0)
turtle.pensize(3)

# Define the colors to use
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Move the turtle to the center
turtle.penup()
turtle.goto(-100, 100)
turtle.pendown()

# Draw the concentric squares 
for i in range(4):
    for i in range(len(colors)):
        turtle.color(colors[i])
        for j in range(4):
            turtle.forward(100 - i * 20)
            turtle.right(90)
    turtle.right(90)


# Hide the turtle
turtle.hideturtle()

turtle.done()
