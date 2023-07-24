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
    
    while True:  # Validation for username length and uniqueness
        username = input("Username: ")
        if len(username) >= 1:
            with open(f"{user}.txt", "r") as file:
                existing_usernames = [line.strip().split('\t')[0] for line in file]
            
            if username in existing_usernames:
                print("Username already exists. Please choose a different username.")
            else:
                data.append(username)
                break
        else:
            print("Username should be at least 1 character.")
    
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
        if user != 'Student':
            break
        else:
            while True:
                form = int(input('Enter Form 1/2/3/4/5 (ONLY 1-5): '))
                if form <= 5:
                    data.append(form)
                    break  # This should be aligned with the inner while loop
                else:
                    print('Please Enter number (1-5)')


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
            EditMenu('Tutor')  # Pass the username and password to the EditMenu function
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

# Start of Receptionist Function
def ReceptionistMenu(username, password): #Reception Menu 
    while True:
        print('Receptionist Menu')
        print("1. Register / Delete Student ")
        print("2. Update Student's enrollment")
        print("3. Payment")
        print('4. Support Ticket')
        print("5. Change Password")
        print('6. Logout\n')

        choice = input("Enter your choice: ")
        if choice == '1': #Done
            EditMenu('Student')  
        elif choice == '2':
            UpdateSub('Student')
        elif choice == '3':
            username = input('Enter Student Name: ')
            Payment('Receptionist', username)
        elif choice == '4':  #Done
            ticket_menu('Receptionist', 'Receptionist')
        elif choice == '5':
            ChangePW('Receptionist' , username, password)
        elif choice == '6':
            return
        else:
            print('Invalid input,please enter number 1 to 6 only.')
            print("")

def Payment(user, username): #can be used by student as well call with Payment()
    # Read student data
    student_data = []
    with open('Student.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                student_info = line.split('\t')
                student_data.append(student_info)

    # Declare and initialize user_name variable and ask for input
    user_name = username

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
        print("\n Total Price for {}: RM{:.2f} \n".format(user_name, total_price))
    elif payable_amount == 0:
        print("\n Payable Amount for {}: RM{:.2f} \n".format(user_name, payable_amount))
    elif payable_amount > 0:
        print("\n Payable Amount for {}: RM{:.2f} \n".format(user_name, payable_amount))
    elif payable_amount < 0:
        print("\n Overpaid for {}: RM{:.2f} \n ".format(user_name, payable_amount))



    if user == 'Receptionist':
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

def create_new_ticket(file_name , username):
    ticket_number = generate_ticket_number(file_name)
    name = username
    message = input('Enter your message: ')
    status = 'Pending'
    
    new_ticket = f'{ticket_number}\t{name}\t{message}\t{status}\n'
    
    with open(file_name, 'a') as file:
        file.write(new_ticket)
    print('This is your ticket number: '+ ticket_number)
    print('Please remember your ticket number.')
    print('New ticket created successfully!')

def remove_ticket(file_name, username):
    ticket_number = input('Enter the ticket number to remove: ')
    name = username
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
            print('Ticket removed successfully! \n')
        else:
            print('Ticket not found or does not belong to you. \n')
    else:
        print('Process Cancelled \n')
     
def change_ticket_status(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        ticket_list = ""
        

    for line in lines:
        ticket_list += line
        if 'Pending' in line:
            print(line.strip())  # Print the line if it has a 'Pending' status

    ticket_number = input('Which ticket number do you want to edit?: ')
    while len(ticket_number) != 3:
        print("Enter a valid ticket number consisting of 3 digits")
        ticket_number = input('Which ticket number do you want to edit?: ')
        

    if ticket_number in ticket_list:
        print('If Approve, enter Y. If Reject, enter N.')
        new_status = input('Enter the new status: ').capitalize()
        while new_status not in ['Y', 'N']:
            print('Invalid input. Please enter Y to Approve or N to Reject.')
            new_status = input('Enter the new status: ').capitalize()

        if new_status == 'N':
            reason = input("Enter your reason: ")
            new_status = "Rejected	Reason:" + reason
        else:
            reason = ""
            new_status = 'Approved'
            
        with open(file_name, 'w') as file:
            for line in lines:
                ticket_info = line.split('\t')
                if ticket_info[0] == ticket_number:
                    if len(ticket_info) == 5:
                        ticket_info.remove(ticket_info[-1])
                        ticket_info.remove(ticket_info[-1])
                    else:
                        ticket_info.remove(ticket_info[-1])
                    ticket_info.append(new_status)
                    updated_line = '\t'.join(ticket_info)
                    file.write(updated_line + '\n')
                else:
                    file.write(line)
            
        print('Ticket status updated successfully.\n')
    else:
        print ("That ticket does not exist.\n")

def check_status(user,username):
    with open('ticket.txt', 'r') as file:
        lines = file.readlines()

    if user == 'Student':
        student_name = username
        for line in lines:
            if student_name in line:
                print('\n'+ line.strip())  # Print the line if the student's name is found
        
        if student_name not in line:
            print('\n You do not have a Ticket \n')
    
    elif user == 'Receptionist':
        pending_ticket_found = False
        for line in lines:
            if 'Pending' in line:
                print('\n' + line.strip() + '\n')  # Print the line if 'Pending' is found
                pending_ticket_found = True

        if not pending_ticket_found:
            print('No Ticket in Pending \n') 

def ticket_menu(user, username):
    
    while True: 
        if user == 'Student':
            print('1. Create new ticket')
            print('2. Remove ticket')
            print('3. Check Status')
            print('4. Return to Student Menu')
            choice = input('Enter Your Choice 1-4: ')
            if choice == '1':
                create_new_ticket('Ticket.txt', username)
            elif choice == '2':
                remove_ticket('Ticket.txt', username)
            elif choice == '3':
                check_status('Student', username)
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
                check_status('Receptionist', 'Receptionist')
            elif choice == '2':
                change_ticket_status('Ticket.txt')
            elif choice == '3':
                return
            else:
                print('Invalid choice. Please try again.')
# End of Receptionist function


# Start of Tutor Function

def ViewEnrolledStudent(username): #Done
    # Read tutor data
    tutor_data = []
    with open('tutor.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                tutor_info = line.split('\t')
                tutor_data.append(tutor_info)

    # Find the tutor's subjects
    tutor_subjects = []
    for tutor_info in tutor_data:
        if tutor_info[0] == username:
            tutor_subjects = tutor_info[4:7]
            break

    # Read student data
    student_data = []
    with open('student.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                student_info = line.split('\t')
                student_data.append(student_info)

    # Find students with the same subjects as the tutor
    students_with_same_subjects = []
    for student_info in student_data:
        for subject in student_info[4:]:
            if subject in tutor_subjects:
                students_with_same_subjects.append(student_info)
                break
    # Sort students by their level
    students_with_same_subjects = sorted(students_with_same_subjects, key=lambda student: int(student[3]))

    # Print the students' information
    print(f"Students under {username}'s class in the following subjects:")
    for student in students_with_same_subjects:
        print(f"StudentID: {student[0]}, Student Name: {student[2]}, Level: {student[3]}")


    print('\n')  # Add a new line for better readability

def add_new_class(username):
    subject = input("Enter the subject: ")
    tutor = username
    day = input("Enter the day of the week (e.g., Monday): ")
    start_time = input("Enter the start time (e.g., 4:00 PM): ")
    end_time = input("Enter the end time (e.g., 5:30 PM): ")
    level = input("Enter the level (e.g., Level 3): ")

    # Format the data into the desired format
    new_class_info = f"Subject:{subject}|Tutor:{username}|Day:{day}|StartTime:{start_time}|EndTime:{end_time}|Level:{level}\n"

    # Append the new class information to the TXT file
    with open('TESTSUB.txt', 'a') as file:
        file.write(new_class_info)

    print("New class added successfully!")

def delete_class(username):
    tutor_name_to_search = f"Tutor:{username}|"

    with open('TESTSUB.txt', 'r') as file:
        lines = file.readlines()

    found_lines = []  # Store the lines that match the targeted username
    for line in lines:
        if tutor_name_to_search in line:
            found_lines.append(line.strip())

    # Print the found lines to the user with line numbers
    for i, line in enumerate(found_lines, 1):
        print(f"Line {i}: {line}")

    if not found_lines:
        print(f"No classes found under the tutor's name '{username}'.")
        return

    # Ask for the line number to delete
    line_number_to_replace = int(input("Enter the line number to delete (or 0 to cancel): "))
    if 0 < line_number_to_replace <= len(found_lines):
        # Find the corresponding line number in the original lines list
        count = 0
        for i, line in enumerate(lines):
            if tutor_name_to_search in line:
                count += 1
                if count == line_number_to_replace:
                    original_line_number = i
                    break

        # Replace the selected line with an empty line
        lines[original_line_number] = '\n'

        # Write the updated data structure back to the text file
        with open('TESTSUB.txt', 'w') as file:
            file.writelines(lines)

        print("Line deleted successfully!")
    elif line_number_to_replace == 0:
        print("No line was deleted.")
    else:
        print("Invalid line number. Please enter a valid line number.")

def edit_class(username):
    tutor_name_to_search = f"Tutor:{username}|"

    with open('TESTSUB.txt', 'r') as file:
        lines = file.readlines()

    found_lines = []  # Store the lines that match the targeted username
    for line in lines:
        if tutor_name_to_search in line:
            found_lines.append(line.strip())

    # Print the found lines to the user with line numbers
    for i, line in enumerate(found_lines, 1):
        print(f"Line {i}: {line}")

    if not found_lines:
        print(f"No classes found under the tutor's name '{username}'.")
        return

    # Ask for the line number to edit
    line_number_to_edit = int(input("Enter the line number to edit (or 0 to cancel): "))
    if 0 < line_number_to_edit <= len(found_lines):
        # Find the corresponding line number in the original lines list
        count = 0
        for i, line in enumerate(lines):
            if tutor_name_to_search in line:
                count += 1
                if count == line_number_to_edit:
                    original_line_number = i
                    break

        # Get the current class information from the selected line
        current_class_info = lines[original_line_number].strip().split('|')
        current_day = current_class_info[2].replace('Day:', '').strip()
        current_start_time = current_class_info[3].replace('StartTime:', '').strip()
        current_end_time = current_class_info[4].replace('EndTime:', '').strip()

        # Ask for new day and time inputs
        new_day = input(f"Current Day: {current_day}\nEnter the new day of the week (e.g., Monday): ")
        new_start_time = input(f"Current Start Time: {current_start_time}\nEnter the new start time (e.g., 4:00 PM): ")
        new_end_time = input(f"Current End Time: {current_end_time}\nEnter the new end time (e.g., 5:30 PM): ")

        # Modify the class information with the new day and time
        new_class_info = f"{current_class_info[0]}|Tutor:{username}|Day:{new_day}|StartTime:{new_start_time}|EndTime:{new_end_time}|{current_class_info[5]}"

        # Replace the selected line with the edited class information
        lines[original_line_number] = new_class_info + '\n'

        # Write the updated data structure back to the text file
        with open('TESTSUB.txt', 'w') as file:
            file.writelines(lines)

        print("Class edited successfully!")
    elif line_number_to_edit == 0:
        print("No class was edited.")
    else:
        print("Invalid line number. Please enter a valid line number.")

def edit_charges(tutor_name):
    # Step 1: Find the subjects the tutor is in charge of in TESTSUB.txt
    tutor_subjects = set()  # Using a set to avoid duplicates
    with open('TESTSUB.txt', 'r') as file:
        for line in file:
            if f"Tutor:{tutor_name}|" in line:
                subject_info = line.split('|')[0].replace('Subject:', '').strip()
                tutor_subjects.add(subject_info)

    if not tutor_subjects:
        print(f"No subjects found for the tutor '{tutor_name}' in TESTSUB.txt.")
        return

    # Step 2: Display current prices for subjects from Subject_Pricing.txt
    current_prices = {}
    with open('Subject_Pricing.txt', 'r') as file:
        for line in file:
            subject, price = line.strip().split('\t')
            current_prices[subject] = int(price)

    # Display current prices to the tutor
    print("Current Prices:")
    for subject in tutor_subjects:
        price = current_prices.get(subject, 'Not found')
        print(f"{subject}: {price}")

    # Step 3: Ask the tutor to choose a subject to edit the pricing
    subject_to_edit = input("Enter the subject to edit the pricing (or 'cancel' to exit): ").capitalize()
    if subject_to_edit== 'Cancel':
        print("Edit charges cancelled.")
        return
    

    # Check if the chosen subject is in the tutor's subjects
    if subject_to_edit not in tutor_subjects:
        print(f"The tutor '{tutor_name}' is not in charge of the subject '{subject_to_edit}'.")
        return

    # Step 4: Take the new pricing input and update Subject_Pricing.txt
    new_price = input(f"Enter the new price for {subject_to_edit}: ")
    try:
        new_price = int(new_price)
        if new_price < 0:
            print("Invalid price. Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid price.")
        return

    # Update the pricing in Subject_Pricing.txt
    with open('Subject_Pricing.txt', 'r') as file:
        lines = file.readlines()

    with open('Subject_Pricing.txt', 'w') as file:
        for line in lines:
            subject, price = line.strip().split('\t')
            if subject == subject_to_edit:
                file.write(f"{subject}\t{new_price}\n")
            else:
                file.write(line)

    print("Pricing updated successfully!")

def ClassMenu(username):
    while True:
        print('\n' 'Class Menu')
        print('1. Add New Class')
        print('2. Delete Class')
        print('3. Edit Class')
        print('4. Edit Charges')
        print('5. Go Back')
        choice = input('Enter Your Choice: ')
        if choice == '1':
            add_new_class(username)
        elif choice == '2':
            delete_class(username)
        elif choice == '3':
            edit_class(username)
        elif choice == '4':
            edit_charges(username)
        elif choice == '5':
            return
        else: 
            print('Invalid input,please enter number 1 to 4 only.')
            print('')


def TutorMenu(username, password):
    while True:
        print('\n')
        print('Tutor Menu')
        print("1. Class Menu ")
        print("2. View Students enrolled in my Class")
        print("3. Change Password")
        print('4. Logout ')

        choice = input("Enter your choice: ")
        if choice == '1': #Done
            ClassMenu(username)  
        elif choice == '2':
            ViewEnrolledStudent(username)
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
def timetable(student_username):
    # Step 1: Find the subjects and levels of the student from Student.txt
    student_subjects = []
    student_level = []
    with open('Student.txt', 'r') as file:
        for line in file:
            data = line.strip().split('\t')
            if data[0] == student_username:
                # Get the subjects starting from the 5th element (index 4) up to the second-to-last element
                student_subjects = [subject for subject in data[4:-1] if subject]
                student_level = 'Level ' + data[3]
                print('\n')
                break

    if not student_subjects:
        print(f"No subjects found for the student '{student_username}' in Student.txt.")
        return

    # Step 2: Display the timetable based on the student's subjects and level from TESTSUB.txt
    print("Timetable for Student:", student_username)
    with open('TESTSUB.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue  # Skip empty lines
            subject_info = line.split('|')
            try:
                if len(subject_info) >= 6:
                    subject = subject_info[0].replace('Subject:', '').strip()
                    tutor = subject_info[1].replace('Tutor:', '').strip()
                    day = subject_info[2].replace('Day:', '').strip()
                    start_time = subject_info[3].replace('StartTime:', '').strip()
                    end_time = subject_info[4].replace('EndTime:', '').strip()
                    level = subject_info[-1].replace('Level:', '').strip()

                    # Check if both the subject and level match the student's subjects and level
                    if subject in student_subjects and level == student_level:
                        print(f"Subject: {subject}, Tutor: {tutor}, Day: {day}, "
                            f"Start Time: {start_time}, End Time: {end_time}, Level: {level}" '\n')
                else:
                    print("Invalid line in TESTSUB.txt:", line)
            except IndexError:
                print("Error processing line in TESTSUB.txt:", line)

def StudentMenu(username, password):
    while True:
        print('Student Menu')
        print('1. Check My Timetable ')
        print('2. Ticket')
        print('3. Check Balance')
        print('4. Change Password')
        print('5. Log Out')
        choice = input('Enter Your Choice (1-5): ')
        if choice == '1':
            timetable(username)
        elif choice == '2':
            ticket_menu('Student' , username)
        elif choice == '3':
            Payment('Student' , username)
        elif choice == '4':
            ChangePW('Student', username, password)
        elif choice == '5':
            return
        else:
            print('Invalid input,please enter number 1 to 5 only.' '\n')
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





#Income (admin) number of subject find price* student in the class1 #done
#Payment for recep and student need double confirm (DONE)
#Search for class func for both tutor and student double check #done
#back button for every page (Need double check)

#register no duplicate username!!!
#ticket system just add username into it and check his own ticket straightaway #fixed
#STUDENT CAN PAY #fixed
