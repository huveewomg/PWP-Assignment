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
        choice = input('Enter Your Choice (1-6): ')
        if choice == '1':
            timetable(username)
        elif choice == '2':
            ticket_menu('Student')
        elif choice == '3':
            Payment('Student')
        elif choice == '4':
            ChangePW('Student', username, password)
        elif choice == '5':
            return
        else:
            print('Invalid input,please enter number 1 to 5 only.' '\n')
            

StudentMenu('Student43', 'password41')
        