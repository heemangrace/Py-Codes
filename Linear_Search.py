""" Linear Search 알고리즘을 implement 한다. """

############################################################
# linear_search:
# input: 리스트 A 와 찾으려는 값 x
# return: 찾았다면 x가 위치해있는 곳의 index를 반환한다. 찾지 못했다면 -1을 반환한다. 
############################################################
def linear_search(A, x):
    for i in range(0, len(A) - 1):
        if (x == A[i]):
            return i
    
    return -1
############################################################


############################################################
""" Script """
############################################################
A = [31, 49, 59, 26, 41, 58]
print(linear_search(A, 41))