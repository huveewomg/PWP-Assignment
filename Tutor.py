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

def search_class_by_subject(subject):
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

def search_class_by_student():
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
                    search_class_by_subject(subject=subject)
                found_student = True
                break

    if not found_student:
        print('Student not found.')

    print('\n')  # Add a new line for better readability

def ClassMenu(user):
    while True:
        print('Class Menu')
        print('1. Check Timetable')
        print('2. Add / Edit Class (Only For Tutor)')
        
        choice = int(input('Enter your choice (1 or 2): '))
        
        if choice == 1:
            print('Do you want to check the timetable for:')
            print('1. A specific student')
            print('2. A specific subject')
            
            search_choice = int(input('Enter your choice (1 or 2): '))
            
            if search_choice == 1:
                student_name = input('Enter student username: ')
                search_class_by_student()
            elif search_choice == 2:
                subject = input('Enter subject: ').capitalize()
                search_class_by_subject(subject=subject)
            else:
                print('Invalid choice. Please try again.')
        elif choice == 2:
            EditClass()
        else:
            print('Invalid choice. Please try again.')





def TutorMenu():
    while True:
        print('Tutor Menu')
        print("1. Add Class Information ")
        print("2. View Students enrolled in my Class")
        print("3. Change Password")

        choice = int(input("Enter your choice: "))
        if choice == 1: #Done
            ClassMenu('Tutor')  
        elif choice == 2:
            tutor_name = input("Enter tutor name: ")
            ViewEnrolledStud(tutor_name)
        elif choice == 3:  #Done
            ChangePW('Tutor')
        else:
            print('Invalid input,please enter number 1 to 3 only.')
            print("")

TutorMenu()