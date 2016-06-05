import turtle

def create_turtle(shape, color):
    new_turtle = turtle.Turtle()
    new_turtle.shape(shape)
    new_turtle.color(color)
    return new_turtle

def draw_square(some_turtle, length):
    x = 0
    while x < 4:
        some_turtle.forward(length)
        some_turtle.right(90)
        x += 1

def draw_circle(some_turtle, radius):
    some_turtle.circle(radius)

def draw_triangle(some_turtle, length):
    for i in range(0,3):
        some_turtle.right(120)
        some_turtle.forward(length)

def draw_diamond(some_turtle, length):
        some_turtle.left(45)
        some_turtle.forward(length)
        some_turtle.left(45)
        some_turtle.forward(length)
        some_turtle.left(135)
        some_turtle.forward(length)
        some_turtle.left(45)
        some_turtle.forward(length)

def draw_super_circle(some_turtle, length):
    for i in range(0, 36):
        draw_square(some_turtle, length)
        some_turtle.right(10)

def draw_flower(some_turtle, length):
    for i in range(0,36):
        draw_diamond(some_turtle, length)
        some_turtle.right(20)
    some_turtle.right(90)
    some_turtle.forward(length * 4)    

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("white")

##    brad = create_turtle("turtle", "yellow")
##    brad.speed(2)
##    draw_square(brad, 100)
##    
##    angie = create_turtle("arrow", "blue")
##    draw_circle(angie, 100)
##    
##    adrian = create_turtle("triangle", "green")
##    draw_triangle(adrian, 100)
##
##    kayo = create_turtle("turtle", "pink")
##    kayo.speed(100)
##    draw_super_circle(kayo, 100)

    kai = create_turtle("turtle", "blue")
    kai.speed(100)
    draw_flower(kai, 50)

    window.exitonclick()

draw_shapes()
