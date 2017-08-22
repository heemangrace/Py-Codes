""" Recursive Merge Sort�� �����Ѵ�. """
################################################################################
# merge: A[low : middle + 1], A[middle + 1 : high] �� ���ĵ� ����Ʈ�� �����Ѵ�. 
# input: ����Ʈ A, index low, middle, high
# return: ���ĵ� ����Ʈ A[low : high + 1]
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
# recursive_merge_sort: A[low: high + 1]�� ����Ʈ�� �����Ѵ�.
# input: ����Ʈ A, ���� low, ���� high
# return: ���ĵ� ����Ʈ A
################################################################################
def recursive_merge_sort(A, low, high):
    # ���� low�� high�� ���̰� 1 �̻��̸� (�� �����ϰ��� �ϴ� ����Ʈ�� ���̰� 2 �̻�)
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