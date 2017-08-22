""" Maximum subarray problem을 brute force로 공략한다. """

def brute_maximum_subarray(A):
    maximum = A[0]
    for i in range(0, len(A) - 1):
        for j in range(i + 1, len(A) - 1):
            if maximum < sum(A[i : j + 1]):
                maximum = sum(A[i : j + 1])
    
    return maximum

A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
print(brute_maximum_subarray(A))