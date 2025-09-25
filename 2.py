a = int(input("Enter an integer: "))

series = []
for i in range(a):
    number = 2 * i + 1
    series.append(str(number))

output = ", ".join(series)
print(output)