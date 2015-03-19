
def saddle_point(matrix):
    col_elements = [] # max
    row_elements = [] # min
    rows_count = len(matrix)

    for row_index in range(rows_count):
        min_elem = min(matrix[row_index])
        count_elems = matrix[row_index].count(min_elem)

        if count_elems == 1:
            index_elem = matrix[row_index].index(min_elem)
            row_elements.append((row_index, index_elem, min_elem))

    print(row_elements)

saddle_point([[8,3,0,1,2,3,4,8,1,2,3],[3,2,1,2,3,9,4,7,9,2,3],[7,6,0,1,3,5,2,3,4,1,1]])

