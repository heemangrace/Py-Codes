""" O(n^2) 의 복잡도로 inversion 을 센다. """
################################################################################
# count_inversion:
# input: 리스트 A
# return: A 내에서의 inversion 횟수
################################################################################
def count_inversion(A):
    counter = 0
    for i in range(0, len(A)):
        for j in range(i + 1, len(A)):
            if A[i] > A[j]:
                counter += 1
    
    return counter
################################################################################


################################################################################
""" Script """
################################################################################
A = [2, 3, 8, 6, 1]
print(count_inversion(A))