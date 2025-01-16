print("Welcome to the menu chatbot!")
name = input("What is your name, user? ")
print("Nice to meet you " + name + "!")
age = input("How old are you " + name +" ?")

while True:
    print("\nHow can I help you today?")
    print("1) Option 1")    
    print("2) Option 2")    
    print("3) Option 3")    
    print("4) Option 4")    
    print("Exit) Exit")
    #
    userChoice = input("Please choose from the list of options shown above or exit (ex: 1): ")
    ##
    if userChoice == "1":
        print("Option 1 selected")
    elif userChoice == "2":
        print("Option 2 selected")
    elif userChoice == "3":
        print("Option 3 selected")
    elif userChoice == "4":
        print("Option 4 selected")
    elif userChoice.lower() == "exit":
        print("Exiting... Goodbye!")
        break
    else:
        print("Oops, invalid choice. Could you pick from the options listed above?")
#print("This is what " + name + " has chosen so far")
