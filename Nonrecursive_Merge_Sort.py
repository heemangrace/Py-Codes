""" Merge Sort를 재귀를 이용하지 않고 한다. """


################################################################################
# merge: 
# input: 리스트 A[low : middle + 1], A[middle + 1 : high + 1]
# return: 두 정렬된 리스트를 합병한다.
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
# nonrecursive_merge_sort:
# input: 리스트 A
# return: 정렬된 리스트 A
################################################################################
def nonrecursive_merge_sort(A):
    
    if (len(A) == 1):
        return
     
    # step 만큼 이루어진 sublist 들로 쪼개고 (남는 것들은 따로 모아 리스트를 구성)
    # 그 리스트 들을 merge 함수를 이용해 병합한다.
    step = 1
    while (1):
        for i in range(0, len(A) // (2 * step)):
            merge(A, i * (2 * step), i * (2 * step) + step - 1, i * (2 * step) + 2*step - 1)
        
        # 자투리 리스트를 병합시킨다.
        merge(A, i * (2 * step), i * (2 * step) + 2*step - 1, len(A) - 1)
        
        # 현재 step 값의 2배가 리스트의 길이보다 커지면 while 문 종료
        if (2 * step) >= len(A):
            break
        else:
            step *= 2
    
    # 마지막으로 커다란 두개의 리스트 병합
    merge(A, 0, step - 1, len(A) - 1)
    
    return
################################################################################



################################################################################
""" Script """
################################################################################
A = [i for i in range(100000, 0, -1)]
nonrecursive_merge_sort(A)

print(A)