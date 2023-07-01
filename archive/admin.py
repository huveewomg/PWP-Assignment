def EditRecep ():  #both read write cant co exist  
    #delete or add 
    print('1. Add new Receptionist')
    print('2. Remove Receptionist')
    choice = int(input('What do you want to do ? '))
    if choice == 1:
        register('Receptionist')
        print('Receptionist added successfully')
    elif choice == 2:
        delete('Receptionist')
        print('Receptionist removed sucessfully')
    
def EditTutor():
    #delete or add 
    print('1. Add new Tutor')
    print('2. Remove Tutor')
    choice = int(input('What do you want to do ? '))
    if choice == 1:
        register('Tutor')
        print('Tutor added successfully')
    elif choice == 2:
        delete('Tutor')
        print('Tutor removed sucessfully')
    
def Edit(user):
    print('1. Add new '+ user)
    print('2. Remove ' + user)
    choice = int(input('What do you want to do ? '))
    if choice == 1:
        register(user)
        print('Tutor added successfully')
    elif choice == 2:
        delete(user)
        print('Tutor removed sucessfully')





def Income(): 
    #implement subject and class first 
    #a rough amount of student are required
    file = open('Income.txt' , 'r')

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

def delete(user):
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




def AdminMenu():
    while True:
        print('Admin Menu')
        print("1. Edit Receptionist")
        print("2. Edit Tutor")
        print("3. Income Report")
        print("4. Change Password")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            Edit('Receptionist')
        elif choice == 2:
            Edit('Tutor')
        elif choice == 3:
            Income()
        elif choice == 4:
            ChangePW('Admin')
        else:
            print('Invalid input,please enter number 1 to 4 only.')
            print("")

AdminMenu()