
def clean_list(list_to_clean):
    result = []

    for i in list_to_clean:
        interrupt = False

        for j in result:
            if type(i) == type(j) and i == j:
                interrupt = True
                break

        if interrupt:
            continue

        result.append(i)

    return result

print(clean_list([1, 2, 1, 1, 3, 4, 5, 4, 6, '2', 7, 8, 9, 0, 1, 2, 3, 4, 5]))