def factorial (n):
    result = 1
    for i in range (1,n+1):
        result *=i
        return result
n=int(input("enter a number:"))
print("factorial of number is:",factorial(n))
