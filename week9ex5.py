def main():
    phrase=input("Enter a sentence: ")
    return count_spaces(phrase)

def count_spaces(entry):
    spaces=0
    for char in entry:
        if char==" ":
            spaces=spaces+1
    return spaces

print(main())
