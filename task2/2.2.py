user_name = str(input("Name: ")).replace(" ", "").split(',')

user_assignments = input("Assignments: ").replace(" ", "").split(',')

user_labs = input("Labs: ").replace(" ", "").split(',')

user_test = input("Test: ").replace(" ", "").split(',')

dict_user = {}

dict_user["name"] = user_name
dict_user["assignments"] = user_assignments
dict_user["labs"] = user_labs
dict_user["test"] = user_test

len_dict = len(dict_user["labs"]) + len(dict_user["assignments"])

print(len_dict)
