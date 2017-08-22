""" 2개의 n-bit 이진수를 받아서, 길이 n+1 의 array에 두 수의 합을 저장한다. """

############################################################################
# binary_sum:
# input: 2 개의 tuple (각각 n 자리) A, B
# return: 2개의 이진수의 합을 저장한 길이 n + 1의 리스트
############################################################################
def binary_sum(A, B):
    # 먼저 항상 A가 B보다 길게 한다. 
    if len(A) < len(B):
        A, B = B, A
    
    # 합을 담을 새로운 리스트를 구성한다.
    b_sum = [None] * (len(A) + 1)
    
    # 각 tuple의 뒷자리 부터 합을 계산해야하므로 i = -1, 받아올림을 체크하는 overflow 
    i = -1
    overflow = 0
    while i >= -len(B):
        b_sum[i] = (A[i] + B[i] + overflow) % 2
        
        if (A[i] + B[i] + overflow) > 1:
            overflow = 1
        else:
            overflow = 0
        
        i -= 1
         
    # B가 끝나고 A 혼자 남았을 경우 
    while i >= -len(A):
        b_sum[i] = (A[i] + overflow) % 2
        
        if (A[i] + overflow) > 1:
            overflow = 1
        else:
            overflow = 0
        
        i -= 1
        
    # 마지막에 새로운 자리가 생기는 지 여부를 overflow로 판단한다. 
    if overflow > 0:
        b_sum[0] = 1
    else:
        b_sum[0] = 0
    
    return b_sum


###########################################################################
""" Script """
###########################################################################
b1 = (1, 1, 1)
b2 = (1, 1, 1, 1)
print(binary_sum(b1, b2))