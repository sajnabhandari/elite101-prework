print("Welcome to the Return and Exchange Assistant!")
print("This chatbot will help you with returning or exchanging your items quickly and easily.")

name = input("Please enter your name: ")
phone_number = input("Please enter the phone number you made your order with: ")

print(f"Thank you, {name}! Let's get started with your request.")
while True:
    print("\nHow can I help you today?")
    print("1) Exchange Item")
    print("2) Return Item")
    print("3) Exchange and Return History")
    print("Exit) Exit")

    userChoice = input("Please choose from the list of options shown above or exit (ex: 1): ")

    if userChoice == "1":
        print("Option 1 selected: Exchange Item")
    elif userChoice == "2":
        print("Option 2 selected: Return Item")
    elif userChoice == "3":
        print("Option 3 selected: Exchange and Return History")
    elif userChoice.lower() == "exit":
        print("Exiting... Goodbye!")
        break
    else:
        print("Oops, invalid choice. Could you pick from the options listed above?")
