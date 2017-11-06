array1 = [5, 2, 6, 3, 1, 0, 4]
print("sorting the following unsorted array using SELECTION SORT")
print(array1);

for i in range(0, len(array1) - 1):
    min = i;
    for j in range(i + 1, len(array1)):
        if array1[j] < array1[min]:
            min = j;
    array1[i], array1[min] = array1[min], array1[i]

print(array1);