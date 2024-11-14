from turtle import *

#we want to paint house

width(5)
color("blue")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)

forward(80)
color("green")
begin_fill()
left(90)
forward(90)
right(90)
forward(50)
right(90)
forward(90)
end_fill()


penup()
goto(200,200)
pendown()

color("red")
begin_fill()
left(215)
forward(170)
left(108)
forward(172)
end_fill()

left(40)

color("blue")
forward(40)
left(87)
forward(3.8)
color("white")
forward(26)
color("gray")
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)

penup()
goto(200,200)
pendown()

color("blue")
left(180)
forward(34)
forward(3.8)
color("white")
right(90)
forward(26)
color("gray")
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)












exitonclick()