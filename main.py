from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

tim = Turtle()
tim.speed("fastest")
tim.hideturtle()

color_list = [(247, 215, 64), (37, 105, 154), (203, 233, 248), (247, 145, 48), (222, 246, 233), (219, 156, 3),
              (240, 42, 73), (162, 24, 60), (86, 186, 223), (30, 185, 129), (165, 86, 29), (250, 63, 24),
              (225, 217, 6), (172, 45, 64), (154, 32, 23), (105, 105, 190), (238, 128, 142), (124, 203, 151),
              (64, 45, 59), (249, 158, 199), (45, 48, 141), (132, 239, 188), (49, 37, 69), (30, 85, 81), (36, 185, 213),
              (111, 213, 238), (50, 126, 101), (238, 168, 159), (170, 191, 220), (82, 38, 33), (38, 65, 62),
              (36, 81, 85), (246, 10, 46), (90, 71, 32)]

y = 0.00

for row in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.pendown()
        tim.penup()
        tim.forward(50)
    y += 50
    tim.goto(0.00, y)

screen.exitonclick()


# import colorgram as c
# 
# rgb_tuples = []
# color_objects = c.extract('image.jpg', 36)
# 
# for item in range(36):
#     single_object_item = color_objects[item]
#     r = single_object_item.rgb[0]
#     g = single_object_item.rgb[1]
#     b = single_object_item.rgb[2]
#     rgb = (r, g, b)
#     rgb_tuples.append(rgb)
# 
# print(rgb_tuples)
