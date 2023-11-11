user_input = input("Input: ").replace(" ", "").split(',')

list_number = []
for number in user_input:
    number = int(number)
    list_number.append(number)

len_list = len(list_number) // 4
list_number.sort()

q1, q2, q3, q4 = [], [], [], []

for x in list_number:
    index = list_number.index(x)
    if len(q1) < len_list:
        q1.append(x)
    elif len(q2) < len_list:
        q2.append(x)
    elif len(q3) < len_list:
        q3.append(x)
    elif len(q4) < len_list:
        q4.append(x)

print(f"{q1}\n{q2}\n{q3}\n{q4}")

