
from turtle import *

def get_num(st):
    digits = ''
    for ch in st:
        if ch.isdigit():
            digits += ch
        else:
            return None
    return digits
def get_num_double(st):
    num1 = get_num(st)
    num2 = get_num(st[len(num1)+1:])
    return int(num1), int(num2)
def turn_left(st):
    num = int(get_num(st))
    left(num)
def turn_right(st):
    num = int(get_num(st))
    right(num)
def draw_square(st):
    num = int(get_num(st))
    down()
    for i in range(0,4):
        forward(num)
        left(90)
    up()
def draw_triangle(st):
    num = int(get_num(st))
    down()
    for i in range(0,3):
        forward(num)
        left(120)
    up()
def draw_circle(st):
    num = int(get_num(st))
    down()
    circle(num)
    up()
def move_forward(st):
    num = int(get_num(st))
    forward(num)
def move_backward(st):
    num = int(get_num(st))
    backward(num)
def pen_up():
    up()
def pen_down():
    down()
def draw_rectangle(st):
    length, width = get_num_double(st)
    down()
    for i in range(0,2):
        forward(length)
        left(90)
        forward(width)
        left(90)
    up()
def draw_polygon(st):
    sides, length = get_num_double(st)
    angle = 360/sides
    down()
    for i in range(0,sides):
        forward(length)
        left(angle)
    up()
def go_to(st):
    x,y = get_num_double(st)
    goto(x,y)
def turtle_color(st):
    num = int(get_num(st))
    if num 

def process_st(st):
    for i in range(len(st)):
        if st[i]== "<":




