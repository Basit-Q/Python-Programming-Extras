print("Hello! Welcome to the grading system")
marks = float(input("Kindly Enter Your Marks:"))
                            #below is the formlua that is needed to calculat the grades
if marks > 80:
    print("Your Grade = A")
elif marks >=60 and marks <=79:
    print("Your Grade = B")
elif marks >=50 and marks <=59:
    print("Your Grade = C")
elif marks >=45 and marks <=49:
    print("Your Grade = D")
elif marks >=25 and marks <=44:
    print("Your Grade = E")
elif marks<=24:
    print("You Failed")
