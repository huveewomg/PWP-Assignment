#Login func done
#Access into subject_pricing to add or remove time table (Reuse )

def ViewEnrolledStud(tutor_name):
    tutor_data = []
    with open('Tutor.txt', 'r') as file:
        for line in file:
            line.strip()
            if line:
                tutor_info = line.split('\t')
                tutor_data.append(tutor_info)

    # Find tutor's name
    tutor_index = None
    for i, tutor_info in enumerate(tutor_data):
        if tutor_info[0] == tutor_name:
            tutor_index = i
            break
    if tutor_index is None:
        print("Tutor not found.")
        return
    
    # Filter tutor's subject in charge
    tutor_subjects = tutor_data[tutor_index][2:]

    # Read student data
    student_data = []
    with open('student.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                student_info = line.split('\t')
                student_data.append(student_info)

    # Create a dictionary to store enrolled students by subject
    enrolled_students = {}
    for subject in tutor_subjects:
        enrolled_students[subject] = []

    # Find the students enrolled in the tutor's subjects
    enrolled_students = {}
    for student_info in student_data:
        student_subjects = student_info[2:]
        common_subjects = set(tutor_subjects).intersection(student_subjects) # use venn diagram concept
        
        # Exclude "N/A" subjects from the common subjects
        common_subjects = [subject for subject in common_subjects if subject != "N/A"] 
        
        if common_subjects:
            for subject in common_subjects:
                if subject not in enrolled_students:
                    enrolled_students[subject] = []
                enrolled_students[subject].append(student_info[0])

    # Display the enrolled students
    if enrolled_students:
        print("Enrolled students in {}'s subjects:".format(tutor_name))
        for subject, students in enrolled_students.items():
            print("Subject {}:".format(subject))
            for student_name in students:
                print(student_name)
    else:
        print("No enrolled students found.")

def search_class_by_subject(subject): #need refine
    with open('TESTSUB.txt', 'r') as file:
        class_data = file.read()

    class_list = class_data.split('\n\n')

    subject_found = False

    for class_info in class_list:
        if subject in class_info:
            print('\n')
            print(class_info)
            print('\n')  # Add a new line for better readability
            subject_found = True

    if not subject_found:
        print('Subject Not Available')

def search_class_by_student():  # need refine need each other to work
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

def EditClass(user):# need fix on searching class to update it filter keyword easily
    while True:
            print('')
            print('1. Add Class')
            print('2. Edit Class')
            choice = input(' Enter Your Choice: ')
            if choice == '1':
                subject = input('Enter the subject: ')
                lecturer = input('Enter the lecturer: ')
                charges = input('Enter the charges (e.g., RM?? per month): ')
                class_schedule = input('Enter the class schedule: ')
                
                # Format the charges line as "Charges: RM80 per month"
                charges_line = 'Charges: RM{} per month'.format(charges)
                
                # Write the class information to the TESTSUB.txt file
                with open('TESTSUB.txt', 'a') as file:
                    file.write('\nSubject: {}\nLecturer: {}\n{}\nClass Schedule: {}\n'.format(subject, lecturer, charges_line, class_schedule))
                
                print('Class added successfully!')
                break
            
            elif choice == '2':
                subject = input('Enter the subject to edit: ').capitalize()
                updated_class_info = ''
                found_subject = False
                
                with open('TESTSUB.txt', 'r') as file:
                    class_data = file.read()
                
                class_list = class_data.split('\n\n')
                
                for class_info in class_list:
                    if subject in class_info:
                        print('')
                        print('Current class information:')
                        print(class_info)
                        print('Enter the updated details:')
                        
                        # Prompt the user for updated information
                        updated_subject = input('Subject: ')
                        updated_lecturer = input('Lecturer: ')
                        updated_charges = input('Charges (e.g., 80): ')
                        updated_schedule = input('Class Schedule: ')
                        
                        # Format the charges line
                        updated_charges_line = 'Charges: RM{} per month'.format(updated_charges)
                        
                        # Create the updated class information string
                        updated_class_info = 'Subject: {}\nLecturer: {}\n{}\nClass Schedule: {}'.format(updated_subject, updated_lecturer, updated_charges_line, updated_schedule)
                        
                        found_subject = True
                        break
                
                if found_subject:
                    # Replace the existing class information with the updated information
                    updated_data = class_data.replace(class_info, updated_class_info)
                    
                    with open('TESTSUB.txt', 'w') as file:
                        file.write(updated_data)
                    
                    print('Class edited successfully!')
                else:
                    print('Subject not found.')

            else:
                print('Invalid choice. Please try again.')

def ClassMenu(user):
    while True:
        print('\n')
        print('Class Menu')
        print('1. Check Timetable')
        
        if user == 'Tutor':  # Assuming the user object has a 'role' attribute
            print('2. Add / Edit Class (Only For Tutor)')
            choice = input('Enter your choice (1 or 2): ')
        else:
            choice = input('Enter your choice: ')
        
        if choice == '1':
            print('Do you want to check the timetable for:')
            print('1. A specific student')
            print('2. A specific subject')
            
            search_choice = input('Enter your choice (1 or 2): ')
            
            if search_choice == '1':
                # student_name = input('Enter student username: ')
                search_class_by_student()
            elif search_choice == '2':
                subject = input('Enter subject: ').capitalize()
                search_class_by_subject(subject=subject)
            else:
                print('Invalid choice. Please try again.')
        elif choice == '2':
            if user == 'Tutor':
                EditClass()
            else:
                print('Access denied. Only tutors can perform this action.')
        else:
            print('Invalid choice. Please try again.')


def TutorMenu():
    while True:
        print('\n')
        print('Tutor Menu')
        print("1. Add Class Information ")
        print("2. View Students enrolled in my Class")
        print("3. Change Password")

        choice = input("Enter your choice: ")
        if choice == '1': #Done
            ClassMenu('Student')  
        elif choice == '2':
            tutor_name = input("Enter tutor name: ")
            ViewEnrolledStud(tutor_name)
        elif choice == '3':  #Done
            ChangePW('Tutor')
        else:
            print('Invalid input,please enter number 1 to 3 only.')
            print("")

TutorMenu()