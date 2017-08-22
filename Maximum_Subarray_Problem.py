""" 수열이 주어졌을 때, 합이 최대가 되는 부분수열을 구한다. """


################################################################################
# max_crossing_subarray:
# input: 수열 A 와 index low, middle, 그리고 high
# return: 걸쳐있는 부분수열의 합의 최대값
################################################################################
def max_crossing_subarray(A, low, middle, high):
    
    # 먼저 left 카운터를 정의하여 A[left : middle + 1] 중 최대를 구한다.
    sub_sum = A[middle]
    left_max_sum = A[middle]
    left_max_index = middle
    for left in range(middle - 1, low - 1, -1):
        sub_sum += A[left]
        if sub_sum > left_max_sum:
            left_max_sum = sub_sum
            left_max_index = left
    
    # right 카운터를 정의하여 A[middle + 1 : right] 중 최대를 구한다. 
    sub_sum = A[middle + 1]
    right_max_sum = A[middle + 1]
    right_max_index = middle + 1
    for right in range(middle + 2, high + 1):
        sub_sum += A[right]
        if right_max_sum < sub_sum:
            right_max_sum = sub_sum
            right_max_index = right
    
    return (left_max_index, right_max_index, left_max_sum + right_max_sum)

################################################################################
# max_subarray:
# input: 수열 (혹은 리스트, tuple) A[low: high + 1]
# output: 합이 최대가 되는 부분 수열의 시작과 끝 index, 그리고 합 
################################################################################
def max_subarray(A, low, high):
    
    # 먼저 low = high 인 경우 (Base)
    if low == high:
        return (low, high, A[low])
    else:
        # 중간 값 middle 정의
        middle = low + (high - low) // 2
        
        # 부분 수열이 온전히 왼쪽 리스트 A[low : middle + 1] 에 속하는 경우
        case1 = max_subarray(A, low, middle)
        # 부분 수열이 온전히 오른쪽 리스트 A[middle + 1 : high + 1] 에 속하는 경우
        case2 = max_subarray(A, middle + 1, high)
        # 부분 수열이 middle을 기준으로 걸쳐있는 경우
        case3 = max_crossing_subarray(A, low, middle, high)
        
        if (case1[2] >= case2[2]) and (case1[2] >= case3[2]):
            return max_subarray(A, low, middle)
        
        if (case2[2] >= case1[2]) and (case2[2] >= case3[2]):
            return max_subarray(A, middle + 1, high)
        
        if (case3[2] >= case2[2]) and (case3[2] >= case1[2]):
            return max_crossing_subarray(A, low, middle, high)

################################################################################



################################################################################
""" Script"""
################################################################################
A = [-1 for i in range(0, 10000)]
print(max_subarray(A, 0, len(A) - 1))