money = int(input("specify the amount of money the person is contributing "))
if money <= 1000:
    print("you cant go to trip")

elif money <= 2000:
    print("you can but you wil not get the food")

elif money <= 3000:
    print("you can but you will not get the room but you will ge the food")

elif money <= 4000:
    print("you can do everything")

else:
    print("thats invalid")