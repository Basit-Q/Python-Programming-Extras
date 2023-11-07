print("Hello! Welcome to the Calculator run on Python!")
print("These are the options currently available: \n"
      "1. Subtract\n"
      "2. Add\n"
      "3. Multiply\n"
      "4. Divide\n")
                                #below are my formulas
def subtract(num1, num2):
    return num1 - num2

def add(num1, num2):
    return num1 + num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2



select = int(input("Kindly select an option from: 1, 2, 3, 4 :"))

number_1 = int(input("Input the first number that you want to use:"))
number_2 = int(input("Input the second number that you want to use:"))

                                #below is the code needed to calculate


if select == 1:
    print("The output of the calculation is:",
          subtract(number_1, number_2))

elif select == 2:
    print("The output of the calculation is:",
          add(number_1, number_2))

elif select == 3:
    print("The output of the calculation is:",
          multiply(number_1, number_2))

elif select == 4:
    print("The output of the calculation is:",
          divide(number_1, number_2))


