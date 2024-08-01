list = [5, 2, 4, 1, 6, 3]

def insertion_sort(list):
    for i in range (1, len(list)):
        key = list[i] # store what must be the ith position

        j = i - 1 # look to element prior to i
        while j >= 0 and list[j] > key:
            list[j + 1] = list[j]
            j -= 1
        
        list[j + 1] = key
        print(list)
    return "Sorted list: " + str(list)

print(insertion_sort(list))