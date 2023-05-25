from turtle import *

penup()

star = Turtle()
goto(40,40)
pendown()

for _ in range(5):
    star.left(144)
    star.fd(100)

exitonclick()
done()
