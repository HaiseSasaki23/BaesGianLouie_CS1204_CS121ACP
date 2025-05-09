perfect_number = int(input())
count = []
for i in range(1, perfect_number):
    if perfect_number % i == 0:
        count.append(i)

sum = sum(count)
if perfect_number == sum:
    print("it's a perfect number")
else:
    print("it's not")