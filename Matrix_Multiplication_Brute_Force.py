""" Matrix Multiplication (Ordinary O(n^2) complexity) �� �����Ѵ�. """


################################################################################
# matrix_multiplication:
# input: ��� A (size: m x k), ��� B (size k x n)
# return: ��� AB (size: m x n)
################################################################################
def matrix_multiplication(A, B):
    
    # size�� ��Ÿ���� �������� �����Ѵ�.
    m = len(A)
    k = len(A[0])
    n = len(B[0])
    
    # ���� ���� �ʴ� ��� ���� ����Ŵ
    if k != len(B):
        print("Dimension mismatch!")
        return
    
    # ���ο� m x n ����� ����
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