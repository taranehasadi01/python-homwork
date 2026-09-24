import random
print("*-*-*-*-welcome to Dungeon Crawler-*-*-*-*")
visited=[]
lives = 100
power = 10
room = 0
escaped = False
while len(visited) <4 and lives > 0:
    player_choice=input("if you ready for keep going enter (lets go) else you can run away and back out of castle with choos (run away) ").lower().strip()
    if player_choice == "lets go":
        print(" _________________________________________________________")
        print("| nice....                                                |")
        print("| there is one castle with 4 room.                        |")
        print("| you most pass them for log out healthy and take the gun |")
        print("|           ------you have 100 lives------                |")
        print("|           ------10 power for fight------                |")
        print("|      room1 : have trap        room2 : have dragon       |")
        print("|      room3 : have gun         room4 : have rest         |")
        print("|          every round you go to a on of the room.        |")
        print("|                if pass them you will win.               |")
        print("|_________________________________________________________|")

        print(" ____")
        print("|room|")
        print("|(?) |")
        print("|____|")
        
        current_room=int(input("enter room's number that you ready go there:"))

        if current_room in visited:
            print("You already visited this room! Choose another one.")
            continue

        if current_room == 1:
            visited.append(current_room)
            print("You step into room 1...")
            input("Press Enter to see what happens...")
            print("you keep to trap ,you lose 25 lives ")
            lives -= 25
            room += 1
            print("you go ",room,"room and","you have ", lives ,"lives for countinue")
            continue

        elif current_room == 2:
            visited.append(current_room)
            print("you are facing a dragon!")
            dragon_health = random.randint(75,85)
            while dragon_health > 0 and lives > 0 :
                player_damage=random.randint(power -5 , power +5)
                dragon_health -= player_damage
                print(f"you hit the dragon for {player_damage}! now dragon health : {dragon_health}")
                input("Press Enter to continue...")

                if dragon_health <= 0:
                    print("dragon is dead!")
                    break
            
                dragon_damage=random.randint(15,25)
                lives -= dragon_damage
                print(f"the dragon hits you for {dragon_damage}!now you lives:{lives}")
                input("Press Enter to continue...")

            if lives <= 0:
                print(" You died fighting the dragon!")
                break

            room +=1
            print("you go ", room , "room and " , lives , "lives you have to continue!")
            continue

        elif current_room == 3:
            visited.append(current_room)
            print("You step into room 3...")
            input("Press Enter to see what happens...")
            print("you found a gun!")
            power +=15
            room += 1
            print("you go ",room,"room and","your power naw is:", power)
            continue

        elif current_room == 4:
            visited.append(current_room)
            print("You step into room 4...")
            input("Press Enter to see what happens...")
            print("you can rest for minuts....and 5 lives plus to your lives")
            lives += 5
            room += 1
            print("you go ",room,"room and","you have", lives , "lives now!")
            continue

        else:
            print("we dont have this room please choice 1,2,3,4") 
            continue  
    elif player_choice == "run away":
        escaped = True
        print(" _________________________________________")
        print("| ok....you can run away from the castle! |")
        print("| bye, and be carefull on the road!       |")
        print("|_________________________________________|")
        break
    else :
        print("wrong answar!pleas tell me your decision again..")

if escaped:
    print("You ran away safely. Maybe next time!")
elif lives > 0:
    print("*****************************************")
    print("* YOU WIN! You escaped the castle alive!*")
    print("*****************************************")
else:
    print(" GAME OVER! The castle claimed you...")
    print("                 *_*                ")
