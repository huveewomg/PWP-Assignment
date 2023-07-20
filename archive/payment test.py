def Payment(is_receptionist=False):
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


Payment('Receptionist')
# Payment()