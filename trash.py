pw=str("gotem")
tries=-1
while tries<4:
    tries=tries+1
    attempt=input("Please enter the password ")
    if attempt==pw:
        tries=tries+1
        print("Accepted. You tried to login",tries,"times")
        break
    if tries==4:
        print("Contact support")
        break
