dict_user1 = {'name': 'Adam', 'assignment': [82, 56, 44, 30], 'test': [78, 77], 'lab': [78.2, 77.2],
              'final_grade': 70.25}
dict_user2 = {'name': 'Kevin', 'assignment': [82, 30], 'test': [], 'lab': [78.2], 'final_grade': 0}

students = {dict_user1["name"]: {k: v for k, v in dict_user1.items() if k != 'name'},
            dict_user2['name']: {k: v for k, v in dict_user2.items() if k != 'name'}}

print(students)
