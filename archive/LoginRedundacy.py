
# Function that are global 
def login(user): #login works for everyone call function with '???'
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
                globals()[menu_function](UserID , Password)  # Call the respective menu function based on the user role
                return False

        print("Incorrect credentials.") 
        attempts += 1
        remaining_attempts = max_attempts - attempts
        print(f"Attempts left: {remaining_attempts}")
        print("")

    file.close()
    print("Maximum login attempts reached.")
    exit()

def ChangePW(user, username, password):
    # read data from respective user files
    user_data = []
    with open(user + ".txt", "r") as file:
        for line in file:
            line = line.strip()
            if line:
                user_info = line.split('\t')
                user_data.append(user_info)

    # Find the user record based on the username
    user_index = None
    for i, user_info in enumerate(user_data):
        if user_info[0] == username:
            user_index = i
            break
    if user_index is None:
        print(user + " username not found.")
        return

    # Prompt for the new password and update the data structure
    while True:
        new_password = input("Enter new password: ")

        if len(new_password) < 6:
            print("Password must be at least 6 characters long. Please enter a different password.")
        elif new_password == password:
            print('New password cannot be the same as the previous password. Please enter a different password.')
        else:
            break

    user_data[user_index][1] = new_password

    # Write the updated data structure back to the text file
    with open(user + ".txt", "w") as file:
        for user_info in user_data:
            file.write("\t".join(user_info) + "\n")

    print("Password updated successfully.")

def AdminMenu(username, password):  # Modify the AdminMenu function to receive username and password
    while True:
        print('Admin Menu')
        print("1. Edit Receptionist")
        print("2. Edit Tutor")
        print("3. Income Report")
        print("4. Change Password")
        print('5. Logout')
        choice = input("Enter your choice: ")
        if choice == '1':
            EditMenu('Receptionist')  # Pass the username and password to the EditMenu function
        elif choice == '2':
            EditMenu('Tutor',)  # Pass the username and password to the EditMenu function
        elif choice == '3':
            IncomeMenu()
        elif choice == '4':
            ChangePW('Admin' ,username, password)  # Pass the username to the ChangePW function
        elif choice == '5':
            return
        else:
            print('Invalid input, please enter number 1 to 5 only.')
            print("")





def ReceptionistMenu(username, password): #Reception Menu 
    while True:
        print('Receptionist Menu')
        print("1. Register / Delete Student ")
        print("2. Update Student's enrollment")
        print("3. Payment")
        print('4. Support Ticket')
        print("5. Change Password")
        print('6. Logout')

        choice = input("Enter your choice: ")
        if choice == '1': #Done
            EditMenu('Receptionist')  
        elif choice == '2':
            UpdateSub('Student')
        elif choice == '3':
            Payment(is_receptionist=True)
        elif choice == '4':  #Done
            ticket_menu('Receptionist')
        elif choice == '5':
            ChangePW('Receptionist' , username, password)
        elif choice == '6':
            return
        else:
            print('Invalid input,please enter number 1 to 6 only.')
            print("")



def TutorMenu(username, password):
    while True:
        print('\n')
        print('Tutor Menu')
        print("1. Add Class Information ")
        print("2. View Students enrolled in my Class")
        print("3. Change Password")
        print('4. Logout ')

        choice = input("Enter your choice: ")
        if choice == '1': #Done
            ClassMenu('Tutor')  
        elif choice == '2':
            tutor_name = input("Enter tutor name: ")
            ViewEnrolledStud(tutor_name)
        elif choice == '3':  #Done
            ChangePW('Tutor', username, password)
        elif choice == '4':
            print('Logout Successful')
            return
        else:
            print('Invalid input,please enter number 1 to 3 only.')
            print("")




def StudentMenu(username, password):
    while True:
        print('Student Menu')
        print('1. Check Timetable')
        print('2. Send / Delete Request')
        print('3. Fee')
        print('4. Change Password ')
        print('5. Logout')
        choice = input('Enter Your Choice: ')
        if choice == '1':
            ClassMenu()
        elif choice == '2':
            ticket_menu()
        elif choice == '3':
            Payment()
        elif choice == '4':
            ChangePW('Student',username, password)
        elif choice == '5':
            print('Logout Successful')
            return

        else:
            print('Invalid input,please enter number 1 to 5 only.')



def mainmenu(): # start screen 
    while True:
        print("**********  Welcome to Brilliant Tuition Centre ☺ **********")
        print("1.Admin")
        print("2.Receptionist")
        print("3.Tutor")
        print("4.Student")
        print('5.Exit')
        choice = input("Enter your choice: ")
        if choice == '1':
            login('Admin')
        elif choice == '2':
            login('Receptionist')
        elif choice == '3':
            login('Tutor')
        elif choice == '4':
            login('Student')
        elif choice == '5':
            exit()
        else:
            print('Invalid input,please enter number 1 to 5 only.')
            print("")




mainmenu()