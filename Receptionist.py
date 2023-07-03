#Login Done
#Register and enroll student done. EditMenu() both register and delete users




def UpdateMenu(user): #Change student's enrollment 
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
    subjects = user_data[user_index][2:]
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
    user_data[user_index][2:] = new_subjects

    # Write the updated data back to the file
    with open(user + ".txt", "w") as file:
        for user_info in user_data:
            file.write('\t'.join(user_info) + '\n')

    print("Subjects updated successfully.")


def PaymentMenu():
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
            subjects = student_info[2:]
            total_price = sum(pricing_info[subject] for subject in subjects)
            break

    # Display the total price
    print("Total Price for {}: RM{:.2f}".format(user_name, total_price))  # checkout interface
    total_price = str(total_price)
    print('Do you want to pay now?')
    choice = input('Yes or No (Enter Y/N): ').capitalize()
    if choice == 'Y':
        print('Which method do you prefer to pay with?')
        print('1. Bank Transfer')
        print('2. E-wallet')
        choice = int(input('Enter only 1/2: '))
        Company_Name = input('What Bank/E-wallet? ').upper()
        acc_num = int(input('Enter your Account Number: '))
        print('Connecting to ' + Company_Name + ' Server...')
    # add chances to fail for realistic purpose without random library 
    #fix later
        print('Offical Receipt of Brilliant Tuition Centre(BTC)') # receipt part
        print('_________________________________________________')
        print(user_name + ': RM'+ total_price)
        print('Paid with: ' + Company_Name)
        print('')
        print('Thank you! ')
        print('')
    else:
        return
    
def Ticket():
    #read available ticket waiting for approval check array in txt file
    ticket_list = []
    with open ('Ticket.txt') as file:
        for line in file:
            ticket_info = line.strip()
            ticket_list.append(ticket_info)
    
    
    


def ReceptionistMenu(): #Reception Menu 
    while True:
        print('Receptionist Menu')
        print("1. Register / Delete Student ")
        print("2. Update Student's enrollment")
        print("3. Payment")
        print('4. Support Ticket')
        print("5. Change Password")


        choice = int(input("Enter your choice: "))
        if choice == 1: #Done
            EditMenu('Student')  
        elif choice == 2:
            UpdateMenu('Student')
        elif choice == 3:
            PaymentMenu()
        elif choice == 4:  #Done
            Ticket()
        elif choice == 5:
            ChangePW('Receptionist')
        else:
            print('Invalid input,please enter number 1 to 4 only.')
            print("")

ReceptionistMenu()