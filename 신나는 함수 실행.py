def w(a, b, c):
    global memoization

    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        if (20, 20, 20) in memoization:
            return memoization[(20, 20, 20)]
        memoization[(20, 20, 20)] = w(20, 20, 20)
        return memoization[(20, 20, 20)]
    elif a < b < c:
        if (a, b, c-1) not in memoization:
            memoization[(a, b, c-1)] = w(a, b, c-1)
        if (a, b-1, c-1) not in memoization:
            memoization[(a, b-1, c-1)] = w(a, b-1, c-1)
        if (a, b-1, c) not in memoization:
            memoization[(a, b-1, c)] = w(a, b-1, c)
        return memoization[(a, b, c-1)] + memoization[(a, b-1, c-1)] - memoization[(a, b-1, c)]
    else:
        if (a-1, b, c) not in memoization:
            memoization[(a-1, b, c)] = w(a-1, b, c)
        if (a-1, b-1, c) not in memoization:
            memoization[(a-1, b-1, c)] = w(a-1, b-1, c)
        if (a-1, b, c-1) not in memoization:
            memoization[(a-1, b, c-1)] = w(a-1, b, c-1)
        if (a-1, b-1, c-1) not in memoization:
            memoization[(a-1, b-1, c-1)] = w(a-1, b-1, c-1)
        return memoization[(a-1, b, c)] + memoization[(a-1, b-1, c)] + memoization[(a-1, b, c-1)] - memoization[(a-1, b-1, c-1)]


memoization = {}
while True:
    a, b, c = map(int, input().split())
    if a == b == c == -1:
        break
    print(f'w({a}, {b}, {c}) = {w(a, b, c)}')