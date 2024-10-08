

def remove_all(original, to_remove):
    my_list = list(original)
    for _ in range(my_list.count(to_remove)):
        my_list.remove(to_remove)
    return my_list


def remove_all(original, to_remove):
    return [item for item in original if item != to_remove]


def remove_all(original, to_remove):
    return list(filter(lambda item: item != to_remove, original))


# ----------------

result = remove_all([1, 2, 3, 4, 5, 2, 3, 2, 3], 2)

print(result)
