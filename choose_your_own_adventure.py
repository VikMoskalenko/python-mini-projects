name = input("Type your name: ")
print("Welcome", name, "to this adventure")

answer = input("You are on dirt road, it has come to an end and you can go left or right. Which way would you like to go?").lower()

if answer == "left":
    answer = input("You come to river, you can walk around or swim: ")
    if answer == "swim":
        print("You swim across amd could be eaten by alligator.....")
    elif answer == "walk":
        print("You can walk gor many miles and be lost on the way....")
    else:
        print("Not a valid question")
elif answer == "right":
     answer = input("You come to the bridge, it looks wobbly, would you like to cross it? or head back?(cross/back)") 
     if answer == "back":
         print("You go back to main road, and loose")
     elif answer == "cross":
         answer = input("You are crossing the bridge and meet a stranger. Would you like to talk with them? (yes/no) ").lower()
         if answer == "yes":
             print("You talk to stranger and he will give you a gold")
         elif answer == "no":
             print("You don`t talk with him, and no gold. You are loose")
         else:
             print("Not valid option")
     else:
         print("not valid option")
         
else:
    print("Not a valid option")
    
print("thank you for trying!")