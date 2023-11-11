strings = "Dias Naryssov".lower()


letters = []

for char1 in strings:

    count = 0

    for char2 in strings:

        if char1 == char2:

            count += 1

    j = (char1, count)
    if j not in letters:
        letters.append(j)

print(letters)








