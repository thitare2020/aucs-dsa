# import turtle as t

from turtle import *
color('red', 'yellow')

begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()


##for x in range(6):
##  t.circle(50)
##  t.circle(80)
##  t.circle(100)
##  t.right(60)
  
##for x in range(4):
##  t.forward(100)
##  t.left(90)
##
##for x in range(4):
##  t.right(90)
##  t.forward(100)
