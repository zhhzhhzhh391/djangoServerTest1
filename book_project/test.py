def test(self,A):
    count = 0
    tmp = A[0]
    res = ""
    for i in range(len(A)):
        if A[i] == tmp:
            count = count + 1
        else:
            res = res + A[i-1] + str(count)
            tmp = A[i]
            count = 1
    res = res+A[len(A)-1] + str(count)
    return res

A = "aabcccccaaa"
print(test(object,A))
