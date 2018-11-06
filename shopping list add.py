shopList=[]
add=str(input("What item is next? "))
while len(add)!=0:
    shopList.append(add)
    add=str(input("What item is next? "))
    if len(add)==0:
        print("Your list is finished:")
        print(shopList)
        break
