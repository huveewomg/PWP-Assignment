def search_subject(subject):
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


subject_input = input("Enter the subject name: ").capitalize()
search_subject(subject_input)

def ClassMenu(user):
    while True:
        print('Class Menu')
        print('1. Check Timetable')
        print('2. Update ')
