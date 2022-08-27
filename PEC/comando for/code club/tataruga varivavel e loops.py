lados= int(input())
angulo = 360/ lados

from turtle import *

speed(11)
shape("turtle")
pensize(6)
color("Red")



for count in range(lados):
    forward(100)
    left(angulo)

done()
