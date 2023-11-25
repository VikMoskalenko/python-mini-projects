import random


top_of_range = input("Type a number : ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <=0:
        print("Please enter the number larger than 0")
        quit()
else:
    print("Type a number next time")
    quit()

random_num = (random.randint(0, top_of_range))
#print(random_num)
guesses = 0

while True:
    guesses += 1
    user_guess = input("make a guess : ")
    if user_guess.isdigit():
      user_guess = int(user_guess)
    else:
       print("Type a number next time")
       continue
    if user_guess == random_num:
      print("you got it")
      break
    else: 
        print("Try one more time")
   
print("You have ", guesses, "guesses")