from turtle import Turtle, Screen

danny = Turtle()
danny.shape("circle")
danny.color("CadetBlue")
for _ in range(4):
    danny.forward(100)
    danny.right(90)

screen = Screen()
screen.exitonclick()
