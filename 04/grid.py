import turtle

count = 0

while(count <= 5):
    turtle.penup()
    turtle.goto(-250,count*100-250)
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    turtle.goto(count*100-250, -250)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(500)
    turtle.right(90)
    count += 1

turtle.exitonclick()
