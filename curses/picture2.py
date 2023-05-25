from turtle import *

fd(30)
left(90)
fd(30)
right(90)
fd(30)
left(90)
fd(30)
right(90)
fd(30)
left(90)
fd(30)
right(90)
fd(30)
color('blue')
begin_fill()
for _ in range (4):
    fd(100)
    left(90)
end_fill()

color('brown')
begin_fill()
left(90)
fd(50)
right(90)
fd(40)
right(90)
fd(50)
end_fill()

color('black') # Крыша
begin_fill()
right(90)
fd(40)
right(90)
fd(100)
right(50)
fd(66)
right(80)
fd(66)
right(140)
fd(100)
end_fill()




# right(50) 
# fd(100)
# left(90)
# left(70)
# fd(60)

penup()
goto(130, 118)
dot()
pendown()
penup()
goto(156, 189)
    
    





exitonclick()
done()