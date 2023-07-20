
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


    student_name = input('Enter student name: ')
    found_student = False

    with open('student.txt', 'r') as file:
        student_data = file.readlines()

    for student_info in student_data:
        student_info = student_info.strip()
        if student_info:
            info_list = student_info.split('\t')
            current_student_name = info_list[0]
            current_student_level = info_list[3]
            subjects = info_list[4:]

            if current_student_name.lower() == student_name.lower():
                print('Timetable for', current_student_name + ':')
                for subject in subjects:
                    search_class_by_subject(subject=subject) #reuse the function
                found_student = True
                break

    if not found_student:
        print('Student not found.')

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



TutorMenu("Tutor2", "12345")


# def search_class_by_student():  # need refine need each other to work