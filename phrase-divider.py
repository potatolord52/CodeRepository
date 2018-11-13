sentence1=str(input("Enter the first short sentence: "))
sentence2=str(input("Enter the second short sentence: "))

words1=sentence1.split()
words2=sentence2.split()
bigSentence=words1+words2
bigSentence.sort(key=str.lower)
print(bigSentence)
print("The length of your sentences is",len(bigSentence))

counterList=bigSentence
print(Counts)

#*: for i in bigSentence
#print("The amount of times each word is mentioned: \n", rfeifojreo)
