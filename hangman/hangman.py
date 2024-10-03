'''
  ### What this program does:
  - Simple Hangman game :)
  - Link to game explanation: https://en.wikipedia.org/wiki/Hangman_(game)

  ### Approach to the project:
  1. Import necessary libraries (in this case: random)
  2. Create ASCII Art for decoration purposes (in art.py)
  3. Set the answer and initial values needed, use random to select answer
  4. Set the initial values for the game value
  5. Create helper functions
  6. Driver program
'''

import random
import words
import art

random_word = random.choice(words.answers)
logo = art.logo
symbol = art.symbol

print(logo)
print(random_word+"\n")

display = []
for _ in random_word:
    display+='_'
  
live = 0

while True:
  if input("Enter 's' to start the game - ")=='s':
    validLive = True
    while(validLive):
      guess = input("Enter your guess character: ").lower()
      cnt = 0
      for i in range(len(random_word)):
        if guess == random_word[i].lower():
          display[i]=guess
          cnt+=1
      
      if cnt==0:
        live+=1
        if live==7:
          print(symbol[live])
          print("You loss the game\n")
          validLive=False
        else:
          print("you loss one more live\n")
          print(symbol[live])
      else:
        if '_' not in display:
          print(display)
          print(random_word)
          print("You Win the game...\n")
          validLive=False
        else:
          print("\nYou hit one more success\n")
          print(display)
          print("\n")
    if validLive==False :
      break
  else:
      print("Please select right keyword ")
      

