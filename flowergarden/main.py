import turtle as t

def draw_flower(x,y,color,pen_size, num_petals,petal_length, stem_length):

    t.penup()
    t.setheading(0)
    t.goto(x,y)
    t.pendown()

    #changes pen color/thickness
    t.pencolor("green") 
    t.pensize(20)

    t.right(90)
    t.forward(stem_length)
    t.backward(stem_length)

    t.pencolor(color)
    t.pensize(30)

    #decide the values for num_petals and num_degrees
    # num_petals = num_petals
    num_degrees = int(360/num_petals)

    #petal movement based on number of degrees
    for i in range(num_petals):
        t.forward(petal_length)
        t.backward(petal_length)
        t.right(num_degrees)

    t.pencolor("orange")
    t.dot(30)

draw_flower(120,120,"blue", 20, 8, 50, 150)
draw_flower(60,60,"purple", 20, 8, 50, 150)
draw_flower(0,0, "pink", 20, 8, 50, 150)