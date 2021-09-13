import turtle

def move_turtle():
    turtle.stamp()
    turtle.forward(50)

def forward_turtle():
    turtle.setheading(90)
    move_turtle()

def backward_turtle():
    turtle.setheading(270)
    move_turtle()

def go_left_turtle():
    turtle.setheading(180)
    move_turtle()

def go_right_turtle():
    turtle.setheading(0)
    move_turtle()

def restart():
    turtle.reset()

turtle.shape("turtle")

turtle.onkey(forward_turtle, 'w')
turtle.onkey(go_left_turtle, 'a')
turtle.onkey(backward_turtle, 's')
turtle.onkey(go_right_turtle, 'd')
turtle.onkey(restart, 'Escape')
turtle.listen()
