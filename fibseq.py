def get_fib(num):
    if num <= 1:
        return num
    else:
        fib = []
        for i in range (2,num):
            fib.append(get_fib(num - 1) + get_fib(num - 2))
        return fib


num = int(input("Enter the number of terms: "))
gg = get_fib(num)
print(f"Fibonacci Series: {gg}")

