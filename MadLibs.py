with open("Mad-Libs-Generator/Story.txt","r") as  file:
    story = file.read()

words = set() # Set of Words from the Story which is going to be Replaced

start_of_word = -1
target_start = '<'
target_end = '>'

for i, char in enumerate(story):

    if char == target_start: # When char == '<'
        start_of_word = i
    
    if char == target_end and start_of_word != -1:
        word = story[start_of_word : i + 1]
        words.add(word) # Adding these Words to the Set
        start_of_word = -1


answers = {} # Creating a Dictionary for Input Answers

for word in words: # Loop to ask for Input Answers
    answer = input("Enter a word for "+ word + ": ")
    answers[word] = answer # Storing each Input to the Answers Dictionary

for word in words:
    story = story.replace(word, answers[word])

print(story) # To Display the modified Story