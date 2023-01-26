from PIL import Image                         # For reading image                 
from time import sleep
from random import randint, shuffle 
from turtle import *



sq_side = 7                                   # Side of square to be drawn for each pixel
margin = 2                                    # Margin between squares
black = (0,0,0)                               # Color to be ignored (background color)
size = sq_side + margin * 2                   # Total size of square to be drawn (including margin)
random_draw = True                            # If True, squares will be drawn in random order
img = Image.open('image_processing/india-final.png')          # Input image file




# Read the input image
pixels = []
colors = set()
for i in range(img.size[0]):
    pixels.append([])
    for j in range(img.size[1]):
        pixels[i].append(img.getpixel((i,j)))
        colors.add(img.getpixel((i,j)))


# Remove background color from colors
colors.remove(black)
colors = list(colors)


# Size of the picture being drawn
xmax, ymax = len(pixels), len(pixels[0])
offset_x = -(xmax * size) // 2
offset_y = -(ymax * size) // 2


# List of coordinates to draw (x, y, color)
# Here, x and y are in turtle coordinates (cartesian form)
coordinates_to_draw = []

for y in range(len(pixels[0])):
    for x in range(len(pixels)):
        if pixels[x][y] == black:
            continue
        coordinates_to_draw.append((
            offset_x + x * size, 
            offset_y + (ymax - 1 - y) * size, 
            pixels[x][y]
        ))

if random_draw:
    shuffle(coordinates_to_draw)



# Initialize turtle and Screen
turtle = Turtle()
screen = Screen()
screen.colormode(255)
turtle.speed(0)
screen.bgcolor(black)
turtle.pendown()
turtle.goto(offset_x, offset_y)
turtle.penup()


# Just for suspense :)
sleep(3)


# Draw the picture
for x, y, col in coordinates_to_draw:
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(col)
    turtle.begin_fill()
    direction = randint(0, 1)
    for i in range(4):
        turtle.forward(sq_side)
        if random_draw and direction:
            turtle.right(90)
        else:
            turtle.left(90)
    turtle.end_fill()


turtle.hideturtle()
exitonclick()
