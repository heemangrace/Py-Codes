""" insertion sort 알고리즘 """
""" Pseudocode
for i = 0 to n - 2                                | c1 | n - 1 |
    min_index = smallest_index(A, i, n - 1)       | c2 | n - 1 | 
    A[i], A[min] = A[min], A[i] (exchange)        | c3 | n - 1 | 

smallest_index(A, i, n - 1):
    max = A[i]                                    | c4 | 1 | 
    for j = i to n - 1                            | c5 | n - i | 
       if temp < A[j]:                            | c6 | n - i |
           max, A[j] = A[j], max (exchange)       | c7 | n - i |
"""
# Total: T(n) = c1(n-1) + (n-1)(sum_{0}^{n-2} c4 + c5(n-i) + c6(n-i) + c7(n-i)) + c3(n-1) = O(n^2)
#############################################################
# smallest_index: 
# input: 리스트 A
# return: A내의 최솟값이 위치한 곳의 index를 반환한다. 
#############################################################
def smallest_index(A, i):
    min_index = i
    for j in range(i + 1, len(A)):
        if A[j] < A[min_index]:
            min_index = j
    
    return min_index
#############################################################

#############################################################
# selection_sort:
# input: 리스트 A
# return: 내림차순으로 정렬된 리스트 A
#############################################################
def selection_sort(A):
    
    for i in range(0, len(A) - 1):
        min_index = smallest_index(A, i)
        A[i], A[min_index] = A[min_index], A[i]
        print(A)
    
    return A
#############################################################



#############################################################
""" Script """
#############################################################
A = [9, 1 , 2, 4, -1, 23 ,3, -11, 22, 4, 10]
selection_sort(A)