pi=0
print("The program will calculate Pi")
length=int(input("How many times do I run the loop? "))
for i in range(0,length):
    pi+=((4.0*(-1)**i)/(2*i+1))
print(pi)
