



# Reverse The Sentence
# Write a program to reverse the sentence wordwise.

# Input:
# You have entered a wrong domain
# Output:
# domain wrong a entered have You



def reverseSentence(sentence):
    list_of_the_words = sentence.split()
    # print(list_of_the_words)
    for i in range(int(len(list_of_the_words)/2)):
        parcial = list_of_the_words[i]
        list_of_the_words[i] = list_of_the_words[len(list_of_the_words)-1-i] 
        list_of_the_words[len(list_of_the_words)-1 - i] = parcial 
    # print(list_of_the_words)
    new_sentence = ""
    for word in list_of_the_words:
        new_sentence += word
        new_sentence += " "
    print(new_sentence)


print(reverseSentence(" developers python for message backwards a is this"))