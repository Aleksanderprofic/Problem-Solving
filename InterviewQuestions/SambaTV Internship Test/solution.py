def solution(A):
    flips_when_0_begins = flips_when_1_begins = 0

    for index, num in enumerate(A):
        if index % 2 == 0:
            if num == 1:
                flips_when_0_begins += 1
            else:
                flips_when_1_begins += 1
        else:
            if num == 0:
                flips_when_0_begins += 1
            else:
                flips_when_1_begins += 1
    return min(flips_when_1_begins, flips_when_0_begins)


print(solution([1, 0, 1, 0, 1, 1]))
print(solution([1, 1, 0, 1, 1]))
print(solution([0, 1, 0]))
print(solution([0, 1, 1, 0]))
print(solution([1]))
print(solution([0]))
