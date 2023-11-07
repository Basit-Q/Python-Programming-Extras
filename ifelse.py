print("Welcome to the odd or even calculator :)")
num = int(input("Kindly Enter a Number: "))
mod = num % 2
if mod > 0:
    print(num, "is an odd number!")
else:
    print(num, "is an even number!")
