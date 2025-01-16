print("Welcome to the mental health awareness Chatbot!")
name = input("What is your name, user? ")
print("Nice to meet you " + name + "!")
age = input("How old are you " + name +" ?")
while True:
    print("How can I help you today? ")
    print("1) option 1")    
    print("2) option 2")    
    print("3) option 3")    
    print("4) option 4")    
    userChoice = input("Please choose from the list of options shown above (ex: 1)")
    if userChoice == "1":
    print("option1")
    elif userChoice == "2":
    print("option2")
    elif userChoice == "3":
    print("option3")
    elif userChoice == "4":
    print("option4")
    else:
     print("Oops, invalid choice. Could you pick from what is listed above?")