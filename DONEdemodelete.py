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
        print(line.strip())  # Print each line separately

    ticket_number = input('Which ticket number do you want to edit? ')
    print('If Approve Enter Y, If Reject Enter N')
    new_status = input('Enter the new status:').capitalize()
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

def EditTicket(user):
    ticket_file = 'tickets.txt'
    
    while True: 
        if user == 'Student':
            print('1. Create new ticket')
            print('2. Remove ticket')
            print('3. Check Status')
            choice = input('Enter Your Choice 1-3: ')
            if choice == '1':
                create_new_ticket('Ticket.txt')
            elif choice == '2':
                remove_ticket('Ticket.txt')
            elif choice == '3':
                check_status('Student')
            else: 
                print('Invalid choice. Please try again.')
        elif user == 'Receptionist':
            print('1. View Ticket Status')
            print('2. Change ticket status')
            choice = input('Enter your choice (1-2): ')
            if choice == '1':
                check_status('Receptionist')
            elif choice == '2':
                change_ticket_status('Ticket.txt')
            else:
                print('Invalid choice. Please try again.')

EditTicket('Receptionist')


#view all ticket for receptionist 
#only pending status 
#receptionist cant generate new ticket
#Done 