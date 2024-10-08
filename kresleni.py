import turtle, random

def spirala():
    for i in range(50):
        turtle.forward(i)
        turtle.left(20)
    turtle.ontimer(turtle.Screen().bye, 2000)

def random_shape():
    turtle.speed(10)
    for i in range(50):
        turtle.forward(random.randint(10, 100))
        turtle.left(random.randint(1, 360))
    turtle.ontimer(turtle.Screen().bye, 2000)
    
def jedna():
    turtle.forward(100)
    turtle.back(50)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(135)
    turtle.forward(70)
    turtle.hideturtle()
    turtle.mainloop()
    
def zprava():
    for i in range(5):
        turtle.write("Hello World!", move=False, align="center", font=("Arial", i+20, "normal"))
        
    turtle.hideturtle()
    turtle.mainloop()
    