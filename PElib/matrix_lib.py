# matrix_lib.py





def rotate_ccw(matrix):
    """Returns a copy of the input 2D matrix, rotated 90deg counterclockwise.
    
        - matrix: The input matrix.
        
    rotate_ccw(matrix: list) -> list"""
    rowlength = len(matrix[0])
    new_matrix = []
    for i in range(rowlength):
        new_matrix.append([row[rowlength-i-1] for row in matrix])
    return new_matrix