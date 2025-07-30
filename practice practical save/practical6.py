for i in range(10):
    if i ==5:
        break
    print(i)


for i in range(10):
    if i ==5:
        continue
    print(i)


for i in  range(5):
    if i ==2:
        pass
    print(i)

while True:
    name =input("enter your name(type exit to stop):")
    if name=="exit":
        break
    print('hello' , name)
