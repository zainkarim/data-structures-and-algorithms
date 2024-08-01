'''
1. Find the smallest item in the list and swap it to the 0th position.
2. Find the second smallest item in the list and switch it to the 1 position
3. Find the 3rd smallest element in the list and switch to the 2 position
4. ...
5. Stop when we have swapped the second largest item into the second to last position
'''
list = [2, 5, 4, 1, 6, 3]
def selection_sort(list):
    for i in range(len(list) - 1): # last item is guaranteed to be largest, therefore only have to go to n-1 position
        min_value = list[i]
        min_index = i
        for j in range(i + 1, len(list)):
            if list[j] < min_value:
                min_value = list[j]
                min_index = j
                j += 1
            else:
                j += 1
        temp = list[i]
        list[i] = min_value
        list[min_index] = temp
        print(list)
    return "Sorted list: " + str(list)

print(selection_sort(list))

'''
i = 0, j = 1
min value = 2
min index = 0

1 @ list[3] < 2 @ list[0]
min value = 1
min index = 3

temp = list[i] (2)
list[i(0)] = min value (1)
list[min index(3)] = 2

[1, 5, 4, 2, 6, 3]

i = 1, j = 2
min value = 5
min index = 1

4 @ list[2] < 5 @ list[1]
min value = 4
min index = 2

2 @ list[3] < 4 @ list[2]
min value = 2
min index = 3

temp = list[i] (5)
list[i(1)] = min value (2)
list[min index (3)] = 5

[1, 2, 4, 5, 6, 3]

i = 2, j = 3
min value = list[i] => list[2] = 4
min index = i = 2

3 @ list[5] < 4 @ list[2]
min value = 3
min index = 5

temp = list[i] => list[2] => 4
list[i] => list[2] = min value(3)
list[min index(5)] = temp(4)

[1, 2, 3, 5, 6, 4]

i = 3, j = 4
min value = list[i] => list[3] = 5
min index = i = 3

4 @ list[5] < 5 @ list[3]
min value = 4
min index = 5

temp = list[i] => list[3] = 5
list[i] => list[3] = min value(4)
list[min index] => list[5] = temp 5

[1, 2, 3, 4, 6, 5]

i = 4, j = 5
min value = 6
min index = 4

5 @ list[5] < 6 @ list[4]
min value = 5
min index = 5

temp = list[i] = list[4] = 6
list[4] = min value(5)
list[5] = temp(6)

[1, 2, 3, 4, 5, 6]




'''