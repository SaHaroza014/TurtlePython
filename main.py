from turtle import Turtle, Screen
import random

Louie = Turtle()
my_screen = Screen()
Louie.shape('turtle')
Louie.color('olive')

# num = int(input("How many sides are there? "))
# col=input("Which color do you want? ")

rand_col = ['black', 'red', 'green', 'blue', 'cyan', 'yellow', 'orange', 'purple', 'pink']
rand_width = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def draw_r(num):#right side
    a = 360 / num
    for i in range(num):
        Louie.forward(100)
        Louie.right(a)

def draw_l(num):#left side
    a = 360 / num
    for i in range(num):
        Louie.forward(100)
        Louie.left(a)


for shape in range(3, 21):
    if shape % 2 == 0:
        draw_l(shape)
        Louie.pencolor(random.choice(rand_col))
        Louie.pensize(random.choice(rand_width))
    else:
        draw_r(shape)
        Louie.pencolor(random.choice(rand_col))
        Louie.pensize(random.choice(rand_width))


print(my_screen.canvheight)
my_screen.exitonclick()
