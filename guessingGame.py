import random

print("This is a guessing game! Good luck!\n")

wordList=["pineapple", "donkey", "purple", "golf","brazilian","guitar"]
#dictionary
wordConversions={"pineapple":"fruit","donkey":"animals","purple":"colors","golf":"sports","brazilian":"nationality","guitar":"instrument"}
guess=""

#add in a count so that they have a finite amount of guesses
guesses_allowed=5
guess_count=0


secretWord=random.choice(wordList)
print("Hint:The word is from the category of "+wordConversions.get(secretWord))

while(guess!=secretWord and guess_count<guesses_allowed):
    print("Guess count remaining is: "+str(guesses_allowed-guess_count))
    guess=input("Enter your guess: ")
    guess_count+=1

if(guess_count>=guesses_allowed and guess!=secretWord):
    print("You ran out of guesses before guessing the secret word which was: "+ secretWord+". You lost!")
elif (guess==secretWord):
    print("You won!!")



