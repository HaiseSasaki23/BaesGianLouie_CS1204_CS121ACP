fibonacci_number = int(input())

sequence = [0, 1]
for i in range(2, fibonacci_number):
    sequence.append(sequence[i - 1] + sequence[i - 2])

print(sequence)