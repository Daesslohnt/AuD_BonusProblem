def find_brute(T, P):
    """Return the lowest index of T at witch substring P begins of -1"""
    n, m = len(T), len(P)
    for i in range(n-m+1):
        k = 0
        while k < m and T[i+k] == P[k]:
            k += 1
        if k == m:
            return i
    return -1

if __name__ == "__main__":
    T = "I have found a dog that was lying on the grass"
    P = "dog"
    print(find_brute(T, P))