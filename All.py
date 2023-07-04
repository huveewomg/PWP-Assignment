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

def register(user):  # Register function for everyone
    data = []
    data2 = []
    
    while True:  # Validation for username length
        username = input("Username: ")
        if len(username) >= 1:  # Check if username length is at least 6 characters
            data.append(username)
            break
        else:
            print("Username should be at least 1 characters.")
    
    while True:  # Validation for password length
        p1 = input("Password: ")
        if len(p1) >= 6:  # Check if password length is at least 8 characters
            break
        else:
            print("Password should be at least 6 characters.")
    
    while True:  # Validation for password match
        p2 = input("Confirm password: ")
        if p1 == p2:
            data.append(p1)
            break
        else:
            print("Passwords don't match. Please try again.")

    while True: #add name function only available for student and lecturer
        if user =='Receptionist':
            break
        else:
            name = input('Enter Your Name: ')
            data.append(name)
            break

    while True: #ask for student's form hence only available for Student
        if user == 'Tutor' or 'Receptionist':
            break
        else:
            form = input('Enter Form 1/2/3/4/5: ')
            data.append(form)
            break

    while True:
        if user == 'Receptionist':
            break
        else:
            print("Enter the Subject Names. If empty, please enter 'n'.")
            for _ in range(3):
                subject = input('Subject Name: ')
                if subject == 'n':
                    data.append('N/A')
                else:
                    data.append(subject)
        break
    
    data2.append(data)
    with open(user + '.txt', 'a') as file:
        for data in data2:
            for x in data:
                file.write(x)
                file.write('\t')  # Use '\t' for tab separation
            file.write('\n')  # Start a new line after writing data
    print("Registration successful.")
    print(user + ' added successfully')

def EditMenu(user): #edit menu for everyone
    print('1. Add new '+ user)
    print('2. Remove ' + user)
    choice = int(input('What do you want to do ? '))
    if choice == 1:
        register(user)
        print('Tutor added successfully')
    elif choice == 2:
        delete(user)
        print('Tutor removed sucessfully')

def delete(user): #delete existing user 
    # Read data from respective user files
    user_data = []
    with open(user + ".txt", "r") as file:
        for line in file:
            line = line.strip()
            if line:
                user_info = line.split('\t')
                user_data.append(user_info)

    # Prompt for the username
    username = input("Enter username: ")

    # Find the user record based on the username
    user_index = None
    for i, user_info in enumerate(user_data):
        if user_info[0] == username:
            user_index = i
            break
    if user_index is None:
        print(user + " username not found.")
        return

    # Verify action
    verify = input("Are you sure you want to delete this user " + username + "? (Y/N) ")
    verify = verify.capitalize()
    if verify == 'Y':
        # Delete the line with the username included
        del user_data[user_index]

        # Write the updated data structure back to the text file
        with open(user + ".txt", "w") as file:
            for user_info in user_data:
                file.write("\t".join(user_info) + "\n")

        print("User " + username + " deleted successfully.")
    else:
        print(user +' deletion canceled.')

def ChangePW(user): #change password for everyone
    # read data from respective user files
    user_data = []
    with open(user + ".txt", "r") as file:
        for line in file:
            line = line.strip()
            if line:
                user_info = line.split('\t')
                user_data.append(user_info)

    # Prompt for the username
    username = input("Enter username: ")

    # Find the user record based on the username
    user_index = None
    for i, user_info in enumerate(user_data):
        if user_info[0] == username:
            user_index = i
            break
    if user_index is None:
        print(user + " username not found.")
        return

    # Prompt for the current password and verify it
    current_password = input("Enter current password: ")
    stored_password = user_data[user_index][1]

    if current_password != stored_password:
        print("Incorrect password.")
        return

    # Prompt for the new password and update the data structure
    while True:
        new_password = input("Enter new password: ")
        if new_password == stored_password:
            print('New password cannot be the same as the previous password. Please enter a different password.')
        else:
            break
    user_data[user_index][1] = new_password

 

    # Write the updated data structure back to the text file
    with open(user + ".txt", "w") as file:
        for user_info in user_data:
            file.write("\t".join(user_info) + "\n")

    print("Password updated successfully.")

def PaymentMenu():# Receptionist func
    # Read student data
    student_data = []
    with open('Student.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                student_info = line.split('\t')
                student_data.append(student_info)

    # Declare and initialize user_name variable and ask for input
    user_name = input("Enter your name: ")

    # Read pricing information
    pricing_info = {}
    with open('Subject_Pricing.txt', "r") as file:
        for line in file:
            line = line.strip()
            if line:
                values = line.split("\t")
                if len(values) == 2:
                    subject, price = values
                    pricing_info[subject] = float(price)

    # Find student by name and calculate total price
    total_price = 0
    for student_info in student_data:
        if student_info[0] == user_name:
            subjects = student_info[4:]
            total_price = sum(pricing_info[subject] for subject in subjects)
            break

    # Display the total price
    print("Total Price for {}: ${:.2f}".format(user_name, total_price))

def UpdateMenu(user): #
    user_data = []
    with open(user + ".txt", "r") as file:
        for line in file:
            line = line.strip()
            if line:
                user_info = line.split('\t')
                user_data.append(user_info)

    # Prompt for the username
    username = input("Enter username: ")

    # Find the user record based on the username
    user_index = None
    for i, user_info in enumerate(user_data):
        if user_info[0] == username:
            user_index = i
            break
    if user_index is None:
        print(user + " username not found.")
        return

    # Fetch the last three data under the username
    subjects = user_data[user_index][4:]
    print("Current subjects:", subjects)

    # Prompt for new subjects
    new_subjects = []
    for i in range(3):
        subject = input("Enter subject {}, ".format(i+1)+ 'If nothing enter n: ')
        subject = subject.capitalize()
        if subject == 'N':
            subject = 'N/A'
            print(subject)
            new_subjects.append(subject)
        else:
            new_subjects.append(subject)

    # Replace the last three data with the new subjects
    user_data[user_index][4:] = new_subjects

    # Write the updated data back to the file
    with open(user + ".txt", "w") as file:
        for user_info in user_data:
            file.write('\t'.join(user_info) + '\n')

    print("Subjects updated successfully.")

def ReceptionistMenu(): #Reception Menu 
    while True:
        print('Receptionist Menu')
        print("1. Register / Delete Student ")
        print("2. Update Student's enrollment")
        print("3. Payment")
        print("4. Change Password")

        choice = input("Enter your choice: ")
        if choice == '1': #Done
            EditMenu('Student')  
        elif choice == '2':
            UpdateMenu('Student')
        elif choice == '3':
            PaymentMenu()
        elif choice == '4':  #Done
            ChangePW('Receptionist')
        else:
            print('Invalid input,please enter number 1 to 4 only.')
            print("")

def AdminMenu(): #Admin Menu All function for admin
    while True:
        print('Admin Menu')
        print("1. Edit Receptionist")
        print("2. Edit Tutor")
        print("3. Income Report")
        print("4. Change Password")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            EditMenu('Receptionist')
        elif choice == 2:
            EditMenu('Tutor')
        elif choice == 3:
            Income()
        elif choice == 4:
            ChangePW('Admin')
        else:
            print('Invalid input,please enter number 1 to 4 only.')
            print("")


def mainmenu(): # start screen 
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