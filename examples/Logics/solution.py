n = int(input())
k = list(map(int, input().split()))


def answer(n, k):
    k = sorted(k, reverse=True)
    for i in range(n - 1):
        if k[i] > i >= k[i + 1]:
            return i + 1
    if k[-1] >= len(k):
        return n
    else:
        return -1


print(answer(n, k))
