
lists = [(1001, 2), (1001, 1), (1003, 2), (1005, 2), (1001, 3), (1007, 1), (1007, 2), (1100, 2), (1003, 2),
         (1001, 1)]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    less = [x for x in arr[1:] if x[0] < pivot[0]]
    equal = [x for x in arr[1:] if x[0] == pivot[0]]
    greater = [x for x in arr[1:] if x[0] > pivot[0]]

    return quick_sort(less) + equal + [pivot] + quick_sort(greater)

new_sorted_list = quick_sort(lists)

dias = {}

for i in new_sorted_list:
    name = i[0]
    find_element = i[-1]

    count = new_sorted_list.count(i)

    if i[0] not in dias:
        dias[name] = {find_element: count, 'mft': find_element, 'lft': find_element}

    else:
        if find_element not in dias[name]:
            dias[name][find_element] = count
        else:
            dias[name][find_element] += count

    if count > dias[name][dias[name]['mft']]:
        dias[name]['mft'] = find_element

    if count < dias[name][dias[name]['lft']]:
        dias[name]['lft'] = find_element

print(dias)
