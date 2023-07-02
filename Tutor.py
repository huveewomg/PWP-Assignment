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



def TutorMenu():
    while True:
        print('Tutor Menu')
        print("1. Add Class Information ")
        print("2. Update/Delete Class Information")
        print("3. View Students enrolled in my Class")
        print("4. Change Password")

        choice = int(input("Enter your choice: "))
        if choice == 1: #Done
            ClassUpdate()  
        elif choice == 2:
            UpdateMenu()
        elif choice == 3:
            tutor_name = input("Enter tutor name: ")
            ViewEnrolledStud(tutor_name)
        elif choice == 4:  #Done
            ChangePW('Tutor')
        else:
            print('Invalid input,please enter number 1 to 4 only.')
            print("")

TutorMenu()