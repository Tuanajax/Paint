from cmath import cos
import math
from re import X
from tkinter import Y
import turtle
Tuan_Scr = turtle.Screen()
Tuan_br = turtle.Turtle()
roof_angle = 45
House_height = 100
roof_x = House_height*0.5
roof_cos = cos(roof_angle)
roof_y = math(roof_x//roof_cos)
for i in range(4):
  Tuan_br.forward(House_height)
  Tuan_br.right(90)
Tuan_br.goto(100,100)