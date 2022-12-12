# Print Matrix elements in Spiral fashion

def rotateMatrix_L(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    # Transpose matrix
    matrix_T = []
    for j in range(columns):
        row = []
        for i in range(rows):
            row.append(matrix[i][j])
        matrix_T.append(row)

    # Revese matrix
    return matrix_T[::-1]


def spiralMatrix(mat):
    for i in range(len(mat[0])):
        ele.append(mat[0].pop(0))
    mat.pop(0)
    if mat == []:
        return
    mat = rotateMatrix_L(mat)
    return spiralMatrix(mat)


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
ele = []
spiralMatrix(matrix)
print(ele)