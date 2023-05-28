def insert_sort(A):
    n = len(A)
    for i in range(1, n):
        temp = A[i]
        j = i - 1
        while j > -1 and A[j] > temp:
            A[j + 1] = A[j]
            j -= 1
        A [j + 1] = temp
    return A

a = list(map(int, input().split()))
print(*insert_sort(a))