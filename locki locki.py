import turtle
screen = turtle.Screen()
screen.bgcolor("pink")
ghalam=turtle.Turtle()
ghalam.color("black")
ghalam.shape("turtle")
ghalam.penup()
ghalam.goto(-300, 300)
ghalam.pendown()
for i in range(1,40):
    ghalam.forward(20)
    ghalam.right(10)

ghalam=turtle.Turtle()
ghalam.color("black")
ghalam.shape("turtle")
ghalam.penup()
ghalam.goto(150, 300)    
ghalam.pendown()
for i in range(1,20):
    ghalam.forward(60)
    ghalam.right(30)

ghalam=turtle.Turtle()
ghalam.color("black")
ghalam.shape("turtle")
ghalam.penup()
ghalam.goto(-300, -50)   
ghalam.pendown()
for i in range(1,15):
    ghalam.forward(100)
    ghalam.right(45)

ghalam=turtle.Turtle()
ghalam.color("black")
ghalam.shape("turtle")
ghalam.penup()
ghalam.goto(150, -50)  
ghalam.pendown()
for i in range(1,13):
    ghalam.forward(130)
    ghalam.right(60)

ghalam.penup()
ghalam.goto(-110, -40)
ghalam.color("purple")
ghalam.write("luky  luky :)", font=("Arial", 20))

turtle.done()
