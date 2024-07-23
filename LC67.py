a = "11"  
b = "1"

a_int = int(a, 2)
b_int = int(b, 2)

sum_int = a_int + b_int

sum_binary = bin(sum_int)[2:]

print(sum_binary)