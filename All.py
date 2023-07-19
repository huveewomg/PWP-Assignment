
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
        if len(p1) >= 6:  # Check if password length is at least 6 characters
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
            form = input('Enter Form 1/2/3/4/5 (ONLY 1-5): ')
            data.append(form)
            break

    while True:
        if user != 'Tutor':
            break
        else:
            valid_level = False
            while not valid_level:
                print ('Assign Tutor to level (If handle every level enter 6)')
                level = int(input('Please enter the level the Tutor is assigned (1-6): '))
                if level < 1 or level > 6:
                    print('Invalid number. Please enter a number between 1 and 6.')
                else:
                    data.append(str(level))
                    valid_level = True
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

    while True: 
        if user != 'Tutor':
            break
        else: 
            salary = input('Enter Salary of Tutor per month: ')
            data.append(salary)
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
    return

def EditMenu(user): #Edit menu for add or remove
    while True:
        print('1. Add new '+ user)
        print('2. Remove ' + user)
        print('3. Go back')
        choice =input('What do you want to do ? ')
        if choice == '1':
            register(user)
        elif choice == '2':
            delete(user)
        elif choice == '3':
            return
        else: 
            print('Invalid Input, Please enter number 1 to 3 only. ')

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


def UpdateSub(user): #Reassign subject menu
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


# Start of Receptionist Function
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

def Payment(is_receptionist=False): #can be used by student as well call with Payment()
    # Read student data
    student_data = []
    with open('Student.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                student_info = line.split('\t')
                student_data.append(student_info)

    # Declare and initialize user_name variable and ask for input
    user_name = input("Enter username: ")

    # Find student by name
    user_index = None
    for i, student_info in enumerate(student_data):
        if student_info[0] == user_name:
            user_index = i
            break

    # Check if student name is found
    if user_index is None:
        print("Student username not found. \n")
        return

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
    payable_amount = None
    for student_info in student_data:
        if student_info[0] == user_name:
            subjects = student_info[4:]
            for subject in subjects:
                if subject in pricing_info:
                    total_price += pricing_info[subject]
                if len(student_info) > 4:
                    last_element = student_info[-1]
                    try:
                        payable_amount = float(last_element)
                    except ValueError:
                        payable_amount = None
            break
    if payable_amount is None:
        print("Total Price for {}: RM{:.2f}".format(user_name, total_price))
    elif payable_amount == 0:
        print("Payable Amount for {}: RM{:.2f}".format(user_name, payable_amount))
    elif payable_amount > 0:
        print("Payable Amount for {}: RM{:.2f}".format(user_name, payable_amount))
    elif payable_amount < 0:
        print("Overpaid for {}: RM{:.2f}".format(user_name, payable_amount))



    if is_receptionist:
        # Allow receptionist to proceed with payment
        print('Do you want to proceed with the payment?')
        choice = input('Yes or No (Enter Y/N): ').capitalize()

        if choice == 'Y':
            amount = float(input('Enter the payment amount: RM'))
            balance = payable_amount - amount if payable_amount is not None else total_price - amount
            print('Which method do you prefer to pay with?')
            print('1. Bank Transfer')
            print('2. E-wallet')
            choice = int(input('Enter only 1/2: '))
            Company_Name = input('What Bank/E-wallet?: ').upper()
            acc_num = input('Enter your Account Number: ')
            print('Connecting to ' + Company_Name + ' Server...')

            # Update the student's payment status and amount
            if payable_amount is not None:
                student_data[user_index][-1] = str(balance)
            else:
                student_data[user_index].append(str(balance))

            # Write updated student data back to the file
            with open('Student.txt', 'w') as file:
                for student_info in student_data:
                    file.write('\t'.join(student_info) + '\n')

            # Print receipt
            print('Official Receipt of Brilliant Tuition Centre (BTC)')
            print('_________________________________________________')
            print(user_name + ': RM' + str(amount))
            print('Paid with: ' + Company_Name)
            print('')
            print('Thank you!')


        
    else:
        # Student can only view the total price, no payment actions allowed
        print('Payment option not available for students.')

def generate_ticket_number(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            
            if lines:
                last_line = lines[-1].strip().split('\t')
                last_ticket_number = int(last_line[0])
                new_ticket_number = last_ticket_number + 1
            else:
                new_ticket_number = 1
                
            return str(new_ticket_number).zfill(3)
    except FileNotFoundError:
        return '001'  # If the file doesn't exist, start with ticket number 001

def create_new_ticket(file_name):
    ticket_number = generate_ticket_number(file_name)
    name = input('Enter your name: ')
    message = input('Enter your message: ')
    status = 'Pending'
    
    new_ticket = f'{ticket_number}\t{name}\t{message}\t{status}\n'
    
    with open(file_name, 'a') as file:
        file.write(new_ticket)
    print('This is your ticket number: '+ ticket_number)
    print('Please remember your ticket number.')
    print('New ticket created successfully!')

def remove_ticket(file_name):
    ticket_number = input('Enter the ticket number to remove: ')
    name = input('Enter Your Name: ')
    confirmation = input('Are you Sure ? (Y/N)').capitalize()

    with open(file_name, 'r') as file:
        lines = file.readlines()
    
    ticket_found = False

    if confirmation == 'Y':
        with open(file_name, 'w') as file:
            for line in lines:
                if line.startswith(ticket_number) and name in line:
                    ticket_found = True
                else:
                    file.write(line)

        if ticket_found:
            print('Ticket removed successfully!')
        else:
            print('Ticket not found or name does not match.')
    else:
        print('Process Cancelled')
     
def change_ticket_status(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    for line in lines:
        if 'Pending' in line:
            print(line.strip())  # Print the line if it has a 'Pending' status

    ticket_number = input('Which ticket number do you want to edit?: ')
    print('If Approve, enter Y. If Reject, enter N.')
    new_status = input('Enter the new status: ').capitalize()

    while new_status not in ['Y', 'N']:
        print('Invalid input. Please enter Y to Approve or N to Reject.')
        new_status = input('Enter the new status: ').capitalize()

    if new_status == 'Y':
        new_status = 'Approved'
    else:
        new_status = 'Rejected'

    with open(file_name, 'w') as file:
        for line in lines:
            ticket_info = line.split('\t')
            if ticket_info[0] == ticket_number:
                ticket_info[-1] = new_status
                updated_line = '\t'.join(ticket_info)
                file.write(updated_line + '\n')
            else:
                file.write(line)
    
    print('Ticket status updated successfully.')

def check_status(user):
    with open('ticket.txt', 'r') as file:
        lines = file.readlines()

    if user == 'Student':
        student_name = input('Enter Your Name: ')
        for line in lines:
            if student_name in line:
                print(line.strip())  # Print the line if the student's name is found
    
    elif user == 'Receptionist':
        for line in lines:
            if 'Pending' in line:
                print(line.strip())  # Print the line if 'Pending' is found

def ticket_menu(user):
    ticket_file = 'tickets.txt'
    
    while True: 
        if user == 'Student':
            print('1. Create new ticket')
            print('2. Remove ticket')
            print('3. Check Status')
            print('4. Return to Student Menu')
            choice = input('Enter Your Choice 1-4: ')
            if choice == '1':
                create_new_ticket('Ticket.txt')
            elif choice == '2':
                remove_ticket('Ticket.txt')
            elif choice == '3':
                check_status('Student')
            elif choice == '4':
                return
            else: 
                print('Invalid choice. Please try again.')
        elif user == 'Receptionist':
            print('1. View Ticket Status')
            print('2. Change ticket status')
            print('3. Return to Receptionist Menu')
            choice = input('Enter your choice (1-3): ')
            if choice == '1':
                check_status('Receptionist')
            elif choice == '2':
                change_ticket_status('Ticket.txt')
            elif choice == '3':
                return
            else:
                print('Invalid choice. Please try again.')

# End of Receptionist function


# Start of Admin Function
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

def IncomeMenu():
    while True:
        print()
        print('Check Income')
        print('1. Check Income based on Level')
        print('2. Check Income based on Subject')
        print('3. Check Profit This Month')
        print('4. Return to Admin Menu')

        choice = input('Enter your Choice (1-4): ')

        if choice == '1':
            level = int(input('Enter the level (1-5): '))
            income = calc_income('level', level)
            print(f"Income per month for Level {level}: RM{income}")
        elif choice == '2':
            subject = input('Enter the subject: ').capitalize()
            income =  calc_income('subject', subject)
            print(f"Income per month for Subject {subject}: RM{income}")
        elif choice == '3':
            calculate_profit()
        elif choice == '4':
            return
        else:
            print('Invalid choice. Please try again.')

def calc_income(option, value):
    # Read student data
    student_data = []
    with open('Student.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                student_info = line.split('\t')
                student_data.append(student_info)

    # Read subject pricing data
    subject_pricing = {}
    with open('Subject_Pricing.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                subject, price = line.split('\t')
                subject_pricing[subject] = int(price)

    # Calculate income per month based on the option
    income = 0
    if option == 'level':
        for student_info in student_data:
            if int(student_info[3]) == value:
                for subject in student_info[4:7]:
                    if subject in subject_pricing:
                        income += subject_pricing[subject]
    elif option == 'subject':
        for student_info in student_data:
            if value in student_info[4:7]:
                if value in subject_pricing:
                    income += subject_pricing[value]

    return income

def calculate_profit():
    tutor_salary = 0
    with open('Tutor.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                tutor_info = line.split('\t')
                if len(tutor_info) > 1:
                    salary = tutor_info[-1]
                    if salary.isdigit():
                        tutor_salary += int(salary)

    total_income = calc_income('level', 1) + calc_income('level', 2) + calc_income('level', 3) + calc_income('level', 4) + calc_income('level', 5)
    total_expenses = float(input('Other expenses such as Rent: '))

    profit = total_income - tutor_salary - total_expenses
    print('\n' + "Total Income: RM{:.2f}".format(total_income))
    print("Total Expenses: RM{:.2f}".format(total_expenses))
    print("Total Salary: RM{:.2f}".format(tutor_salary))
    print("Profit: RM{:.2f}".format(profit))

# End of Admin Function


# Start of Tutor Function
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

# End of Tutor Function


# Start of Student Function
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



# End of Student Function




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

#Income (admin) number of subject find price* student in the class1
#Payment for recep and student need double confirm (DONE)
#Search for class func for both tutor and student double check
#back button for every page (Need double check)
