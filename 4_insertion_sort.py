array = [64, 34, 22, 11, 3, 9, 90]

n = len(array)
for i in range(1,n):
    insert_index = i
    current_value = array.pop(i)
    for j in range(i-1, -1, -1):
        if array[j] > current_value:
            insert_index = j
    array.insert(insert_index, current_value)

print("Sorted array:", array)