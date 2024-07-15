# linear search
def linear_search(list, key):
    index = 0
    while index < len(list):
        if key == list[index]:
            return index
        else:
            index += 1
    return None
