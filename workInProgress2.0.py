shopLst={}
def main():
    print("""A list has been created.
Add items by typing them in, confirming, then typing price, confirming.
To remove an item: type 'remove', press Enter, type name,press Enter.
To see the list and prices: type 'seeList'
To see total price: type 'totalPrice'
To clear the list: type 'clearList'.
To end the list: type 'end'.""")
    bigPrice=0
    element="-"
    processor(element)
    element=input("")

def processor(element):
    if element=="remove":
        removable=input("")
        for x in shopLst:
            if x==removable:
                shopLst.pop(removable)
            else:
                return "Cannot find item"
    elif element=="seeList":
        return shopLst
    elif element=="totalPrice":
        return "%.2f"%bigPrice
    elif element=="clearList":
        shopLst.clear()
    elif element!="remove" and element!="seeList" and element!="totalPrice" and element!="clearList" and element!="end":
        cost=input("")
        shopLst[element]=cost
        bigPrice=bigPrice+cost
    elif element=="end":
        return "List finished"

main()
