numbers = [2,2,2,6,2,2,2,2]
sum = 0
for num in numbers:
    if num % 2 == 0:
        sum += num
print(sum)

n = 10
sum_even = 0

for i in range(1, n+1):
    if i%2 == 0:
        sum_even += i

print("Sum of even number is: , ", sum_even)