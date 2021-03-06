""" Strassen의 행렬 곱셈 알고리즘을 실행한다. 복잡도: O(n^(log_{2}^{7})) """


################################################################################
# strassen: 
# input: n x n 행렬 A 와 B
# return: 행렬 A와 B의 곱 AB
################################################################################
def strassen(A, B):
    
    # Base Case: 길이가 1일 때
    if len(A) == 1:
        return A[0][0] * B[0][0]
    
    # Recursive Case: 길이가 2 이상일 때
    middle = len(A) // 2 - 1
    A11 = A[2:3]
    slice