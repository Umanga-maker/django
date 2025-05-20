discount = 0
amount = 400


if amount > 1000:
    discount = amount * 10 / 100
elif amount > 500 and amount <= 1000:
    discount = amount * 5 / 100
elif amount > 200 and amount <= 500:
    discount = amount * 2 / 100
else:
    discount = 0

print("amount = ", amount - discount)

