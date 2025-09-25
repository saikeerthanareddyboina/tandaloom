numbers = [1,2,8,9,12,46,76,82,15,20,30]
counts = {i: 0 for i in range(1, 10)}
for divisor in counts.keys():
    for num in numbers:
        if num % divisor == 0:
            counts[divisor] += 1

print(counts)