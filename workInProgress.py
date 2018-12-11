shopLst={}
bigPrice=0
def main():
    print("A list has been created. Add items by typing them in, confirming, then typing price, confirming.\nTo remove an item: type 'remove', press Enter, type name, press Enter.\nTo see the list and prices: type 'seeList'.\nTo see total price: type 'totalPrice'.\nTo clear the list: type 'clearList'.\nTo end the list: type 'end'.")
    element=input("")
    while element!="end":
        processor(element)
        element=input("")
    else:
        return "List finished"
def processor(element):
    if element=="remove":
        for removable in shopLst:
            if element==removable:
                shopLst.pop(removable)
            else:
                return "Cannot find item"
    elif element=="seeList":
        return shopLst
    elif element=="totalPrice":
        return "%.2f"%bigPrice
    elif element=="clearList":
        shopLst.clear()
    else:
        cost=input(float(""))
        shopLst[element]=cost
        bigPrice=bigPrice+cost

print(main())
