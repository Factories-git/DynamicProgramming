n = int(input())
kg = 0
while n % 5 != 0 and n >= 3:
    n -= 3
    kg += 1
if n % 5 == 0:
    kg += n // 5
else:
    kg = -1
print(kg)