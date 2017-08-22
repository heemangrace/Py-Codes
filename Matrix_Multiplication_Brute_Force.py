""" Matrix Multiplication (Ordinary O(n^2) complexity) 를 수행한다. """


################################################################################
# matrix_multiplication:
# input: 행렬 A (size: m x k), 행렬 B (size k x n)
# return: 행렬 AB (size: m x n)
################################################################################
def matrix_multiplication(A, B):
    
    # size를 나타내는 변수들을 설정한다.
    m = len(A)
    k = len(A[0])
    n = len(B[0])
    
    # 정의 되지 않는 경우 에러 일으킴
    if k != len(B):
        print("Dimension mismatch!")
        return
    
    # 새로운 m x n 행렬을 만듦
    C = [ [0] * n for i in range(m)]
    for i in range(0, m):
        for j in range(0, n):
            for l in range(0, k):
                C[i][j] += A[i][l] * B[l][j]
    
    return C
################################################################################



################################################################################
""" Script """
################################################################################
A = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
B = [[2, 0, 0], [0, 2, 0]]
print(matrix_multiplication(A, B))