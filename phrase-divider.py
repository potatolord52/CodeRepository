#Asks for sentences
sentence1=str(input("Enter the first short sentence: "))
sentence2=str(input("Enter the second short sentence: "))

#Splits sentences according to whitespaces, adds the two together for a word total
words1=sentence1.split()
words2=sentence2.split()
bigSentence=words1+words2

#Sorts sentence in alphabetical order, using (key=str.lower) to ignore caps, prints
bigSentence.sort(key=str.lower)
print(bigSentence)
print("The length of your sentences is",len(bigSentence))

#Checks if words are in the list, and keeps count on the dictionary
counterList={}
for x in bigSentence:
    if x in counterList:
        counterList[x]=counterList[x]+1
    else:
        counterList[x]=1
    
#Prints item count list
print("The amount of times each word is mentioned: \n",counterList)
