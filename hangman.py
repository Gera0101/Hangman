import time
import random
import symbol
from symbol import stages
from words import word_list 
chosen = random.choice(word_list)
letters = []
lives = 6
for i in chosen:
  letters += i
blank = []
for i in chosen:
  blank += "_" 
print(symbol.logo)
time.sleep(1)
print("\nმოგესალმებით Hangman ში თქვენ უნდა გამოიცნოთ სიტყვა ასოებით მიხედვით")
while blank != letters:
  ask = input("\nშეიყვანეთ ასო: ")        
  if ask in blank:
        print(f"\nშენ უკვე გამოიცანი ასო {ask}")
  for letter in range(0, len(chosen)):
    if ask in letters[letter]:
      blank[letter] = ask
  print("\n",blank)
  if ask not in chosen:       
        lives -= 1
        print(f"\nვერ გამოიცანო, დაგრჩა {lives} ცდა")
        if lives == 0:
              print("\n უი სამწუხაროდ წააგე :(")
              break
if blank == letters:
  print("\nგილოცავ შენ გამოიცანი სიტყვა :)")
  
  
  
  