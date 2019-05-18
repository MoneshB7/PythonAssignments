def form_triangle(num1,num2,num3):
    if (num1 + num2 <= num3) or (num1 + num3 <= num2) or (num2 + num3 <= num1):
        failure="Triangle can't be formed"
        return failure
    else:
        success="Triangle can be formed"
        return success

#Provide different values for the variables, num1, num2, num3 and test your program
num1=2
num2=3
num3=8
message = form_triangle(num1, num2, num3)
print(message)
