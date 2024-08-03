import random
import turtle

from tkinter import simpledialog


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # TODO 1) Create a new Turtle
    my_turtle = turtle.Turtle()
    turtle.pensize(10)
    pen_color = simpledialog.askstring('hi', 'which color would you like to draw with?')
    if pen_color == 'red':
        turtle.pencolor('red')
    elif pen_color == 'orange':
        turtle.pencolor('orange')
    elif pen_color == 'yellow':
        turtle.pencolor('yellow')
    elif pen_color == 'green':
        turtle.pencolor('green')
    elif pen_color == 'blue':
        turtle.pencolor('blue')
    elif pen_color == 'purple':
        turtle.pencolor('purple')
    else:
        sdf = get_random_color()
        turtle.pencolor(sdf)


    for i in range(4):
        turtle.forward(100)
        turtle.left(90)




    #      2) Make the turtle draw a shape (this will take more than one line
    #         of code)
    #      3) Set the pen width to 10
    #      4) Ask the user what color pen they would like to draw with
    #      5) Use an if/else statement to set the pen color that the user
    #         requested
    #      6) If the user doesn't enter anything, choose a random color
    #      7) Put a loop around your code so that you keep asking the user for
    #         more colors & drawing them

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
