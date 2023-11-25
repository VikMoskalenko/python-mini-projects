print("Welcome to my computer quiz")
playing = input("Do you wanna play the game?")
if playing.lower() != "yes":
    quit()
    
print("Okay. Let`s start :) ")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct")
    score += 1
else:
    print("You are not right. ")
    
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct")
    score += 1
else:
    print("You are not right. ")
    
answer = input("What does RAM stand for? ").lower()
if answer.lower() == "random access memory":
    print("Correct")
    score += 1
else:
    print("You are not right. ")
    
print("You have " + str(score) + " questions correct") 
print("You have " + str((score/3) * 100) + " % ") 

    

