
def saddle_point(matrix):

    def get_col(index):
        col = []
        for row in matrix:
            col.append(row[index])
        return col

    rows_count = len(matrix)

    if rows_count == 0:
        return False

    col_elements = [] # max
    row_elements = [] # min

    for row_index in range(rows_count):
        min_elem = min(matrix[row_index])
        count_elems = matrix[row_index].count(min_elem)

        if count_elems == 1:
            index_elem = matrix[row_index].index(min_elem)
            row_elements.append((row_index, index_elem))

    cols_count = len(matrix[0])

    for col_index in range(cols_count):
        column = get_col(col_index)
        max_elem = max(column)
        count_elems = column.count(max_elem)

        if count_elems == 1:
            index_elem = column.index(max_elem)
            col_elements.append((index_elem, col_index))

    for point in col_elements:
        if point in row_elements:
            return point

    return False

print(saddle_point([[21]]))

