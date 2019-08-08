def countingsort(A,B,k):
    # Create histogram of A in C
    C = []
    for i in range(0,k+1):
        C.append(0)
    for j in range(0,len(A)):
        C[A[j]] = C[A[j]] + 1
    # C[i] now contains the number of elements equal to i

    for i in range(1,k+1):
        C[i] = C[i] + C[i-1]
    # C[i] now contains the number of elements less than or equal to i

    for j in range(len(A)-1,-1,-1):
        B[C[A[j]]-1] = A[j]     # every associated index of C must -1
        C[A[j]] = C[A[j]] - 1
