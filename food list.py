food_list=["burger","pizza","frize","pasta","chiken"]
food_price=[10 , 8 , 7, 6 , 10]
drink_list=["orange juise" , "apple juise" ,"coca" ,"soda"]
drink_price=[3 , 2 , 3 , 1]
user_name=str(input("enter your name:"))
order_name=[]
order_price=[]
while True:
    print ("1. order food:")
    print ("2. order drink:")
    print ("3. faktor")
    print ("4. exit")
    choice_number=int(input("choose number:"))
    if choice_number ==1:
        for i in range (0 ,5):
            print( food_list[i] , " : " , food_price[i])
        user_choice=str(input("choose your food:"))
        order_name.append(user_choice)
        i=food_list.index(user_choice)
        order_price.append(food_price[i])
    elif choice_number == 2:
        for i in range (0 ,4):
            print( drink_list[i] , " : " , drink_price[i])
        user_choice=str(input("choose your drink:"))
        order_name.append(user_choice)
        i=drink_list.index(user_choice)
        order_price.append(drink_price[i])

    elif choice_number ==3:
        for i in range (0,len(order_name)):
            print(order_name[i] , order_price[i])
        print("---------------------------------")
        print("total price" , sum(order_price))
    
    elif choice_number == 4:
        print("good bye.")
        break
