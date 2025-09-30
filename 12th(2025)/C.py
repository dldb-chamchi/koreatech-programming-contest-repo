for _ in range(int(input())):
    N, K = map(int, input().split())

    circle = list(map(int, input().split()))

    left, right = 0, N-1

    while left < N:
        result = circle[left] + circle[right]
        if result == K:
            print(left, right)
            break
        elif result > K:
            right -= 1
        else:
            left += 1

