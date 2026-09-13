def namayesh_kala(l):
    for i in l :
        print(i)
def kharid(d):
    user=input("add kala ro entekhab kon")
    return d[user][0],d[user][1]
def jame_kharid(l1,l2):
    for i in range(0,len(l1)):
        print(l1[i]," : ",l2[i])
    print("------------------------")
    print("gheymat kol : ", sum(l2))
esmkala=["1.shekar=10","2.ghand=12","3.cola=60","4.pastil=75","5.chips=145","6.pofak=210","7.abnabat=34"]

kala={"1":[10,"shekar"],"2":[12,"ghand"],"3":[60,"cola"],"4":[75,"pastil"],"5":[145,"chips"],"6":[210,"pofak"],"7":[34,"abnabat"]}
kalaye_entekhabi=[]
gheymat_entekhab=[]
while True:
    print("-------khosh amadid--------")
    print("1. namayesh kalaha")
    print("2. kharid")
    print("3. jame kharid")
    print("4. khoroj ")

    user_choice=int(input("gozine ra entekhab kon:"))
    if user_choice ==1:
        namayesh_kala(esmkala)
    elif user_choice ==2:
        t,z=kharid(kala)
        kalaye_entekhabi.append(z)
        gheymat_entekhab.append(t)
    elif user_choice==3:
        jame_kharid(kalaye_entekhabi,gheymat_entekhab)
    elif user_choice==4:
        print("bye")
        break
    else:
        print("meghdar na motabar!")
while True:
    y_or_n=input("namayesh meno(y) ya khoroj(n)")
    if y_or_n == "y":
        continue
    elif y_or_n == "n":
        print("bye")
    break
