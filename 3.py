a = int(input("Enter an integer: "))

if a % 2 == 0:
    a -= 1
series = [str(2 * i + 1) for i in range(a)]

output = ", ".join(series)
print(output)