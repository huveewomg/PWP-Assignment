def login(user):
    file = open(user + '.txt', "r")
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        UserID = input("User ID: ")
        Password = input("Password: ")

        file.seek(0)  # Reset the file pointer to the beginning
        for line in file.readlines():
            login_info = line.strip().split('\t')  # Split after a tab distance
            if UserID == login_info[0] and Password == login_info[1]:
                file.close()
                print("Correct credentials!")
                print("Welcome " + UserID + "!")
                print("")
                menu_function = user + "Menu"
                globals()[menu_function]()  # Call the respective menu function based on the user role
                return False

        print("Incorrect credentials.")
        attempts += 1
        remaining_attempts = max_attempts - attempts
        print(f"Attempts left: {remaining_attempts}")
        print("")

    file.close()
    print("Maximum login attempts reached.")
    print("")
    mainmenu()
    return False

def AdminMenu():
    print('Admin')

def ReceptionistMenu():
    print('Receptionist')

def TutorMenu():
    print('Tutor')

def StudentMenu():
    print('Student')


def mainmenu():
    while True:
        print("**********  Welcome to Brilliant Tuition Centre ☺ **********")
        print("1.Admin")
        print("2.Receptionist")
        print("3.Tutor")
        print("4.Student")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            login('Admin')
        elif choice == 2:
            login('Receptionist')
        elif choice == 3:
            login('Tutor')
        elif choice == 4:
            login('Student')
        else:
            print('Invalid input,please enter number 1 to 4 only.')
            print("")
            mainmenu()

    
mainmenu()