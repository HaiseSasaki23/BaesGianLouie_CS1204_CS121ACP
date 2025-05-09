money = int(input("Enter the amount of money: "))
orig = str(input("Enter the original currency (USD, EUR, or JPY): "))
target = str(input("Enter the target currency (USD, EUR, or JPY): "))

if orig == "USD" and target == "EUR":
    final = money*0.84

print (f"{final :.2f}")