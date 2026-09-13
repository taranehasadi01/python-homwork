while True:
        try:
            pay=int(input("punch payment:"))
            if pay >= 50000 :
                finally_price = pay * 0.8
                print("pardakhti shoma fh 20% :",finally_price)
            elif pay < 50000 and pay > 20000 :
                finally_price = pay * 0.9
                print("pardakhti shoma ba 10% :",finally_price)
            else :
                finally_price = pay
                print(finally_price)
                print("takhfif roye kalaye shoma emal nashod.")

        except ValueError:
            print("pleas inter number!")
        edame=input("do you want push number again?(y/n)")
        if edame == "y":
            continue
        elif edame == "n":
            break
        else:
            print("invalid choice!")
        

