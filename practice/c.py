
def wiggleSort(nums):
    nums.sort()  # 배열을 오름차순으로 정렬합니다.
    n = len(nums)
    mid = (n - 1) // 2  # 중앙 인덱스 계산

    # 정렬된 배열을 두 부분으로 나누고, 작은 부분과 큰 부분을 나눠서 번갈아가며 배치합니다.
    small_part = nums[:mid + 1][::-1] #지정 안함 (첫번쨰 부터 끝까지 :: 역순 -1)
    large_part = nums[mid + 1:][::-1]

    # 결과 배열을 초기화합니다.
    result = [0] * n

    # 작은 부분과 큰 부분을 번갈아가며 결과 배열에 배치합니다.
    result[::2] = small_part #처음 : 끝 : 간격
    result[1::2] = large_part

    # 결과 배열을 원본 배열에 복사합니다.
    nums[:] = result

output1 = []
output2 = []
for i in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    wiggleSort(nums)
    output1.append(n)
    output2.append(nums)

for i in range(n):
    print(output1[i])
    print(*output2[i])

