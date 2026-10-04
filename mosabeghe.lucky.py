import turtle
import random

def step_turtle(x,y,color):
    ghalam=turtle.Turtle()
    ghalam.color(color)
    ghalam.shape("turtle")
    ghalam.penup()
    ghalam.goto(x,y)
    ghalam.pendown()
    return ghalam

def move_straight(t, step):
    t.forward(step)

def move_gentle_curve(t, step):
    t.circle(80, step // 2)
    t.circle(-80, step // 2)

def move_sharp_curve(t, step):
    t.circle(20, step)
    t.circle(-20, step)

screen=turtle.Screen()
screen.bgcolor("lightblue")
finish_line=300

t1=step_turtle(-300,300,"blue")
t2=step_turtle(-300,0,"purple")
t3=step_turtle(-300,-300,"black")

while True:
    try:
        user_choose=int(input("choos one lucky(1/2/3):"))
        if user_choose in[1,2,3]:
            break
        else:
            print("please enter 1 or 2 or 3:")
    except ValueError:
        print("invalid choice")

while True:
    step = random.randint(10, 30)
    move_straight(t1, step)

    step = random.randint(10, 30)
    move_gentle_curve(t2, step)
    
    step = random.randint(10, 30)
    move_sharp_curve(t3, step)

    if t1.xcor() >= finish_line:
        winner = 1
        break
    elif t2.xcor() >= finish_line:
        winner = 2
        break
    elif t3.xcor() >= finish_line:
        winner = 3
        break

print(f"lucky {winner} won the race!")

if winner == user_choose:
    print("you guessed right! 🎉")
else:
    print("wrong guess, better luck next time!")

turtle.done()

