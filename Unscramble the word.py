import random
from random import choice

print("****WELCOME TO SCRAMBLED WORDS GAME****")
print("A clue is given. Unscramble the word using the clue.")

with open("bacteria.txt","r") as file:
   lines = file.readlines()
   words={}
   for line in lines:
      word, hint= line.strip().split(':')
      words[word.strip()] = hint.strip()
print(words)

#guess = input("Player  guess: ")

#def answer():
 # while True:
  #  if guess.lower() != word.lower():
   #   guess= input("Wrong answer.Try again: ")
    #else:
     # print("correct!") 
      #break 
while True:
   
   word, hint = random.choice(list(words.items()))
   jumbledWord = list(word)
   random.shuffle(jumbledWord)
   #print(jumbledWord)
   jumbled = ''.join(jumbledWord)

   print("Clue: ", hint)
   print("Unscramble this: ",jumbled)
   guess = input("Your guess: ")
   def answer():
     while True:
       guess= input("Wrong answer.Try again: ")
       if guess.lower() == word.lower():
          print("Correct!") 
          break 
       else:
          print("Wrong again. The correct answer is", word) 
          break
       
   if guess.lower() == word.lower():
      print("Absolutely correct!!")
      
   if guess.lower() != word.lower():
      guess=answer()
      
   play_again = input("Play again? (yes/no): ")

   if play_again.lower() != "yes":
    print("Bye bye")
    break
   
