digits = [9]

b = ""

for i in digits:
    b += str(i)

b = int(b) + 1

res = [int(x) for x in str(b)]

print(res)

