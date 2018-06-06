from turtle import *
speed(-1)
x = 50
for i in range(400):
    for i in range(4):
        forward(x)
        left(90)
    right(2)
    x += 2
mainloop()