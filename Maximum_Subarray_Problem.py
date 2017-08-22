""" ������ �־����� ��, ���� �ִ밡 �Ǵ� �κм����� ���Ѵ�. """


################################################################################
# max_crossing_subarray:
# input: ���� A �� index low, middle, �׸��� high
# return: �����ִ� �κм����� ���� �ִ밪
################################################################################
def max_crossing_subarray(A, low, middle, high):
    
    # ���� left ī���͸� �����Ͽ� A[left : middle + 1] �� �ִ븦 ���Ѵ�.
    sub_sum = A[middle]
    left_max_sum = A[middle]
    left_max_index = middle
    for left in range(middle - 1, low - 1, -1):
        sub_sum += A[left]
        if sub_sum > left_max_sum:
            left_max_sum = sub_sum
            left_max_index = left
    
    # right ī���͸� �����Ͽ� A[middle + 1 : right] �� �ִ븦 ���Ѵ�. 
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
# input: ���� (Ȥ�� ����Ʈ, tuple) A[low: high + 1]
# output: ���� �ִ밡 �Ǵ� �κ� ������ ���۰� �� index, �׸��� �� 
################################################################################
def max_subarray(A, low, high):
    
    # ���� low = high �� ��� (Base)
    if low == high:
        return (low, high, A[low])
    else:
        # �߰� �� middle ����
        middle = low + (high - low) // 2
        
        # �κ� ������ ������ ���� ����Ʈ A[low : middle + 1] �� ���ϴ� ���
        case1 = max_subarray(A, low, middle)
        # �κ� ������ ������ ������ ����Ʈ A[middle + 1 : high + 1] �� ���ϴ� ���
        case2 = max_subarray(A, middle + 1, high)
        # �κ� ������ middle�� �������� �����ִ� ���
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