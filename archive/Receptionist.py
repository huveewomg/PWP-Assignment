















def RecepMenu():
    while True:
        print('Receptionist Menu')
        print("1. Register new Student ")
        print("2. Edit Tutor")
        print("3. Income Report")
        print("4. Change Password")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            Edit('Receptionist')
        elif choice == 2:
            Edit('Tutor')
        elif choice == 3:
            Income()
        elif choice == 4:
            ChangePW('Admin')
        else:
            print('Invalid input,please enter number 1 to 4 only.')
            print("")
