users = ["Billy Joe Bob", "D. Vader", "Travis The Ridiculous Security System", "A Person", "Anonymous", "[name]"]


while True:
    print("Hello I'm Travis the Ridiculous Security System.")
    name = input("What is your name? ").strip().lower().title()
    if name in users:
        print("Welcome!")
        remove = input("Would you like to be removed from the list? ").strip().lower()[0] == 'y'
        if remove:
            users.remove(name)
            print("Sorry to see you go.")
        else:
            print("I didn't really want to see you go anyways")
    else:
        print("Sorry I don't recognize you.")
        add = input("Would you like to be added to the system? ").strip().lower() == "y"
        if add:
            users.append(name)
            print("Welcome to my list of friends!")
        else:
            print("Well maybe next time then. Take care.")
