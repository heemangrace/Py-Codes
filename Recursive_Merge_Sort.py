""" Recursive Merge Sort를 실행한다. """
################################################################################
# merge: A[low : middle + 1], A[middle + 1 : high] 두 정렬된 리스트를 병합한다. 
# input: 리스트 A, index low, middle, high
# return: 정렬된 리스트 A[low : high + 1]
################################################################################
def merge(A, low, middle, high):
    # 임시로 값을 저장할 리스트를 생성함
    temp = [None] * (high - low + 1)
    
    # 왼쪽 리스트 (low ~ middle)의 카운터 left, 오른쪽 리스트의 카운터 right 정의
    left = low
    right = middle + 1
    temp_index = 0
    while (left <= middle and right <= high):
        if A[left] < A[right]:
            temp[temp_index] = A[left]
            left += 1
        else:
            temp[temp_index] = A[right]
            right += 1
            
        temp_index += 1
    # 만약 왼쪽 리스트가 모두 소진된 경우 오른쪽 리스트의 나머지를 가져다 붙인다.
    if left > middle:
        temp[temp_index :] = A[right : high + 1]
    else:
        temp[temp_index :] = A[left : middle + 1]
    # temp를 A에 가져다 붙여넣기
    A[low : high + 1] = temp
    return   
################################################################################


################################################################################
# recursive_merge_sort: A[low: high + 1]의 리스트를 정렬한다.
# input: 리스트 A, 하한 low, 상한 high
# return: 정렬된 리스트 A
################################################################################
def recursive_merge_sort(A, low, high):
    # 만약 low와 high의 차이가 1 이상이면 (즉 정렬하고자 하는 리스트의 길이가 2 이상)
    if (high - low) >= 1:
        middle = low + (high - low) // 2
        recursive_merge_sort(A, low, middle)
        recursive_merge_sort(A, middle + 1, high)
        merge(A, low, middle, high)
        
    if low == high:
        return
################################################################################



################################################################################
""" Script """
################################################################################
A = [i for i in range(10000, 0, -1)]
recursive_merge_sort(A, 0, len(A) - 1)
print(A)