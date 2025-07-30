num = int(input("enter a number."))

if num<=1:
    print("neither prime nor composite")
elif num==2:
    print("prime number")
else:
    for i in range(2,num):
        if num% i==0:
            print("composite number")
            break
    else:
        print("prime number")
