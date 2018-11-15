no_one=float(input("Put your first number: "))
no_two=float(input("Put your second number: "))
simp=input("Would you like a simplified answer or not? (Y/N) ")
result=no_one*no_two
short_result=("%.2f"%result)
while simp!="Y" and simp!="N":
    simp=input("Would you like a simplified answer or not? (Y/N) ")
if simp=="Y":
    print("I will now multiply the two numbers")
    print("The result is",short_result)
    print("Thank you for using my program")
if simp=="N":
    print("I will now multiply the two numbers")
    print("The result is",result)
    print("Thank you for using my program")
