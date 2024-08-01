# linear search
def linear_search(list, key):
    index = 0 # c1
    while index < len(list): # c2n
        if key == list[index]:
            return index
        else:
            index += 1

    return None # c3
