""" Merge Sort�� ��͸� �̿����� �ʰ� �Ѵ�. """


################################################################################
# merge: 
# input: ����Ʈ A[low : middle + 1], A[middle + 1 : high + 1]
# return: �� ���ĵ� ����Ʈ�� �պ��Ѵ�.
################################################################################
def merge(A, low, middle, high):
    # �ӽ÷� ���� ������ ����Ʈ�� ������
    temp = [None] * (high - low + 1)
    
    # ���� ����Ʈ (low ~ middle)�� ī���� left, ������ ����Ʈ�� ī���� right ����
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
    # ���� ���� ����Ʈ�� ��� ������ ��� ������ ����Ʈ�� �������� ������ ���δ�.
    if left > middle:
        temp[temp_index :] = A[right : high + 1]
    else:
        temp[temp_index :] = A[left : middle + 1]
    # temp�� A�� ������ �ٿ��ֱ�
    A[low : high + 1] = temp
    return 
################################################################################



################################################################################
# nonrecursive_merge_sort:
# input: ����Ʈ A
# return: ���ĵ� ����Ʈ A
################################################################################
def nonrecursive_merge_sort(A):
    
    if (len(A) == 1):
        return
     
    # step ��ŭ �̷���� sublist ��� �ɰ��� (���� �͵��� ���� ��� ����Ʈ�� ����)
    # �� ����Ʈ ���� merge �Լ��� �̿��� �����Ѵ�.
    step = 1
    while (1):
        for i in range(0, len(A) // (2 * step)):
            merge(A, i * (2 * step), i * (2 * step) + step - 1, i * (2 * step) + 2*step - 1)
        
        # ������ ����Ʈ�� ���ս�Ų��.
        merge(A, i * (2 * step), i * (2 * step) + 2*step - 1, len(A) - 1)
        
        # ���� step ���� 2�谡 ����Ʈ�� ���̺��� Ŀ���� while �� ����
        if (2 * step) >= len(A):
            break
        else:
            step *= 2
    
    # ���������� Ŀ�ٶ� �ΰ��� ����Ʈ ����
    merge(A, 0, step - 1, len(A) - 1)
    
    return
################################################################################



################################################################################
""" Script """
################################################################################
A = [i for i in range(100000, 0, -1)]
nonrecursive_merge_sort(A)

print(A)