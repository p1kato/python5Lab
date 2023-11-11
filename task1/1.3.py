
strings = "Pulp Fiction".lower()

letters = []

glas = []

letter_symbols = []

letter_glass = []

letter_soglass = []

for i in ("aeiouy"):
    glas.append(i)



for char1 in strings:

    count = 0

    for char2 in strings:

        if char1 == char2:

            count += 1

    j = (char1, count)

    if j not in letters:
        letters.append(j)


# k = ["d", 2]

for k in letters:

    charick = k[0]

    if charick == " ":
        letter_symbols.append(k)
    elif charick in glas:
        letter_glass.append(k)
    else:
        letter_soglass.append(k)

print(letter_symbols)
print(letter_glass)
print(letter_soglass)









