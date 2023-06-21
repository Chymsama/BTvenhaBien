#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle

# Khởi tạo màn hình đồ họa
screen = turtle.Screen()
screen.bgcolor('pink')

# Vẽ ngôi nhà
house = turtle.Turtle()
house_color = 'white'
house.fillcolor(house_color)
house.penup()
house.goto(0, -150)
house.pendown()
house.begin_fill()
for _ in range(4):
    house.forward(200)
    house.left(90)
house.end_fill()

# Vẽ mái nhà
roof = turtle.Turtle()
roof_color = 'red'
roof.fillcolor(roof_color)
roof.penup()
roof.goto(200, 50)
roof.pendown()
roof.begin_fill()
roof.goto(100, 150)
roof.goto(0, 50)
roof.end_fill()

# Vẽ cửa sổ
window = turtle.Turtle()
window_color = 'lightblue'
window.fillcolor(window_color)
window.penup()
window.goto(25, -50)
window.pendown()
window.begin_fill()
for _ in range(4):
    window.forward(60)
    window.left(90)
window.end_fill()

window.penup()
window.goto(125, -50)
window.pendown()
window.begin_fill()
for _ in range(4):
    window.forward(60)
    window.left(90)
window.end_fill()

# Vẽ mặt trời
sun = turtle.Turtle()
sun_color = 'yellow'
sun.fillcolor(sun_color)
sun.penup()
sun.goto(200, 200)
sun.pendown()
sun.begin_fill()
sun.circle(100)
sun.end_fill()

# Vẽ cây
tree = turtle.Turtle()
tree_color = 'brown'
tree.fillcolor(tree_color)
tree.penup()
tree.goto(-300, -200)
tree.pendown()
tree.begin_fill()
tree.forward(80)
tree.left(90)
tree.forward(200)
tree.left(90)
tree.forward(80)
tree.left(90)
tree.forward(200)
tree.left(90)
tree.end_fill()

tree.penup()
tree.goto(-250, 0)
tree.pendown()
tree_color = 'green'
tree.fillcolor(tree_color)
tree.begin_fill()
tree.circle(100)
tree.end_fill()

# Ẩn con rùa
house.hideturtle()
roof.hideturtle()
window.hideturtle()
sun.hideturtle()
tree.hideturtle()

# Hoàn thành vẽ
turtle.done()


# In[ ]:




