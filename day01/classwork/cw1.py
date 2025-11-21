#drawing a palace
from turtle import *


width(7)
color("pink")
begin_fill()
forward(300)

left(90)
forward(300)
left(90)
forward(300)
left(90)
forward(300)
right(90)
forward(300)
right(90)
forward(200)
right(90)
forward(300)
left(90)
forward(100)
end_fill()



color("red")
begin_fill()
left(30)


penup()
goto(100,100)
right(120)
pendown()
color("red")
begin_fill()
forward(60)
right(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)
end_fill()


penup()
goto(3,200)
left(60)
pendown()
color("purple")
begin_fill()
forward(200)
left(65)
forward(165)
right(30)
end_fill()



penup()
goto(5,200)
right(90)
forward(100)
right(70)
pendown()
color("green")
begin_fill()
forward(130)
right(25)
forward(185)
right(90)
forward(50)
end_fill()





















exitonclick()