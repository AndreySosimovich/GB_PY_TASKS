a1 = 2
d = 3
n = 4
progressive = [a1 + (i - 1) * d for i in range(1, n + 1)]
print(*progressive, sep='\n')
