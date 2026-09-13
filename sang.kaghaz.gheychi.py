x_win=0
y_win=0
def bazi ():
    global x_win , y_win
    print("halatha: 1.sang 2.kaghaz 3.gheychi.")
    turn_x=input("bazikin x.shomare halat ro entekhab kon:")
    turn_y=input("bazikin y.shomare halat ro entekhab kon:")
    if turn_x == turn_y:
        print ("mosavi,try again")
    elif turn_x == "1" and turn_y == "2":
        y_win = y_win + 1
    elif turn_x == "1" and turn_y == "3":
        x_win = x_win + 1
    elif turn_x == "2" and turn_y == "1":
        x_win = x_win + 1
    elif turn_x == "2" and turn_y == "3":
        y_win = y_win + 1
    elif turn_x == "3" and turn_y == "1":
        y_win = y_win + 1
    elif turn_x == "3" and turn_y == "2":
        x_win = x_win + 1
    else:
        print("vorodi ghalat ast")
    print(f"emtiaz : x = {x_win} , y = {y_win}")

while True:
    bazi()
    if x_win ==3 :
        print("x 3 bar bord va barande shod")
        break
    elif y_win ==3 :
        print("y 3 bar bord va barandeh shod")
        break

    

