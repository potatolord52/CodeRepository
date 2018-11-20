def isEven(var):
    if var%2==0:
        return True
    else:
        return False

if isEven(page):
    print(page)
else:
    print("%60s%d" % (" ", page))
