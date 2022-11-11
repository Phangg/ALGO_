a, b = input().split()
x = int('0b'+a, 2)
y = int('0b'+b, 2)
z = x + y
z = format(z, 'b')
print(z)