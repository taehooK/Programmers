def solution(A, B):
    A.sort()
    B.sort()

    a_max = len(A) - 1
    a_min = 0
    b_max = len(B) - 1
    b_min = 0

    sum = 0

    for i in range(len(A)):
        value = 0
        if A[a_max] > B[b_max]:
            value = A[a_max] * B[b_min]
            a_max -= 1
            b_min += 1
        else:
            value = B[b_max] * A[a_min]
            b_max -= 1
            a_min += 1
        sum += value

    return sum