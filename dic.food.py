food ={"pizza":6 , "kabab":8 , "chicken":4 , "frize" :2}
drink ={"coca" :2 , "soda":1 , "water" :0 , "orange juice":3}
order_name=[]
order_price=[]
print("1. food")
print("2. drink")
print("3. exxit")
user_choice=str(input("choose your order:"))
if user_choice == 1:
    for i in food:
        print(i , ":" , food[i])
        food_order=str(input("writ your food:"))
        order_name.append(food_order)
        order_price.append(food[food_order])
elif user_choice == 2:
    for i in drink:
        print(i , ":" , drink[i])
        drink_order=str(input("writ your drink:"))
        order_name.append(drink_order)
        order_price.append(drink[drink_order])
else:
    print("bye")
