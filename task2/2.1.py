

user_name = str(input("Name: ")).replace(" ", "").split(',')

user_assignments = input("Assignments: ").replace(" ", "").split(',')

user_labs = input("Labs: ").replace(" ", "").split(',')

user_test = input("Test: ").replace(" ", "").split(',')

dict_user = {"name": user_name, "assignments": user_assignments, "labs": user_labs, "test": user_test}

print(dict_user)
