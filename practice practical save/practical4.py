for i in range(1,11):
    print(f"2x {i} = {2*i}")


marks = float(input("enter your marks:"))

if marks>= 101:
    print("invalid input")

elif marks >=90:
    print("grade a")

elif marks>=75:
    print("grade b")

elif marks>=50:
    print("grade c")

elif marks>=35:
    print("grade d")

else:
    print("fail")
