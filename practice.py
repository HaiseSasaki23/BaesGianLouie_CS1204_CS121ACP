def digit_product(n):
    product = 1
    for digit in str(n):
        if digit != '0':  # Ignore zeros
            product *= int(digit)
    return product

# Taking user input
n = int(input("Enter N: "))
print(f"Digit Product: {digit_product(n)}")
