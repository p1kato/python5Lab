user_name = str(input("Name: ")).replace(" ", "").split(',')
user_assignments = input("Assignments: ").replace(" ", "").split(',')
user_labs = input("Labs: ").replace(" ", "").split(',')
user_test = input("Test: ").replace(" ", "").split(',')

dict_user = {}

dict_user["name"] = user_name
dict_user["assignments"] = [int(x) for x in user_assignments]
dict_user["labs"] = [int(x) for x in user_labs]
dict_user["test"] = [int(x) for x in user_test]
def result(assignments, labs, test):
    return (sum(assignments) / 2 * 0.3) + (sum(labs) / 2 * 0.5) + (sum(test) / 2 * 0.2)

print(result(dict_user["assignments"], dict_user["labs"], dict_user["test"]))
