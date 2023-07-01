#so far contain login 
def AdminLogin():
    file = open("Admin.txt", "r")
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        AdminID = input("Admin ID: ")
        Password = input("Password: ")

        file.seek(0)  # Reset the file pointer to the beginning
        for line in file.readlines():
            login_info = line.strip().split('\t')  # Split after a tab distance
            if AdminID == login_info[0] and Password == login_info[1]:
                print("Correct credentials!")
                print("Welcome " + AdminID + "!")
                print("")
                AdminMenu()
                file.close()
                return False

        print("Incorrect credentials.")
        attempts += 1
        remaining_attempts = max_attempts - attempts
        print(f"Attempts left: {remaining_attempts}")
        print("")

    print("Maximum login attempts reached. KYS")
    print("")
    mainmenu()
    file.close()
    return False

 
def AdminMenu():
       while True:
        print('Admin Menu')
        print("1. Register Tutor")
        print("2. Delete Tutor")
        print("3. Register Receptionist")
        print("4. Delete Receptionist")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            AdminLogin()
        elif choice == 2:
            ReceptionistLogin()
        elif choice == 3:
            TutorLogin()
        elif choice == 4:
            StudentLogin()
        else:
            print('Invalid input,please enter number 1 to 4 only.')
            print("")
            mainmenu()

def ReceptionistLogin(): #only role allowed to make account
    file = open("Receptionist.txt", "r")
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        ReceptionistID = input("Receptionist ID: ")
        Password = input("Password: ")

        file.seek(0)  # Reset the file pointer to the beginning
        for line in file.readlines():
            login_info = line.strip().split('\t')  # Split after a tab distance
            if ReceptionistID == login_info[0] and Password == login_info[1]:
                print("Correct credentials!")
                print("Welcome " + ReceptionistID + "!")
                print("")
                AdminMenu()
                file.close()
                return False

        print("Incorrect credentials.")
        attempts += 1
        remaining_attempts = max_attempts - attempts
        print(f"Attempts left: {remaining_attempts}")
        print("")

    print("Maximum login attempts reached. KYS")
    print("")
    mainmenu()
    file.close()
    return False

def ReceptionistMenu():
    print('Done')
    
def TutorLogin(): #only login no register account 
    file = open("Tutor.txt", "r")
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        TutorID = input("Tutor ID: ")
        Password = input("Password: ")

        file.seek(0)  # Reset the file pointer to the beginning
        for line in file.readlines():
            login_info = line.strip().split('\t')  # Split after a tab distance
            if TutorID == login_info[0] and Password == login_info[1]:
                print("Correct credentials!")
                print("Welcome " + TutorID + "!")
                print("")
                TutorMenu()
                file.close()
                return False

        print("Incorrect credentials.")
        attempts += 1
        remaining_attempts = max_attempts - attempts
        print(f"Attempts left: {remaining_attempts}")
        print("")

    print("Maximum login attempts reached. KYS")
    print("")
    mainmenu()
    file.close()
    return False

def TutorMenu():
    print('Done')
    
def StudentLogin(): #only login no register account 
    file = open("Student.txt", "r")
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        StudentID = input("Student ID: ")
        Password = input("Password: ")

        file.seek(0)  # Reset the file pointer to the beginning
        for line in file.readlines():
            login_info = line.strip().split('\t')  # Split after a tab distance
            if StudentID == login_info[0] and Password == login_info[1]:
                print("Correct credentials!")
                print("Welcome " + StudentID + "!")
                print("")
                StudentMenu()
                file.close()
                return False

        print("Incorrect credentials.")
        attempts += 1
        remaining_attempts = max_attempts - attempts
        print(f"Attempts left: {remaining_attempts}")
        print("")

    print("Maximum login attempts reached. KYS")
    print("")
    mainmenu()
    file.close()
    return False

def StudentMenu():
    print('Done')

def mainmenu():
    while True:
        print("**********  Welcome to Brilliant Tuition Centre ☺ **********")
        print("1.Admin")
        print("2.Receptionist")
        print("3.Tutor")
        print("4.Student")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            AdminLogin()
        elif choice == 2:
            ReceptionistLogin()
        elif choice == 3:
            TutorLogin()
        elif choice == 4:
            StudentLogin()
        else:
            print('Invalid input,please enter number 1 to 4 only.')
            print("")
            mainmenu()

    
mainmenu()
    
    