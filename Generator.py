def generator(total_credit):
    remaining_credit = total_credit
    while remaining_credit != 0:
        payment = yield remaining_credit
        remaining_credit -= payment
    exit()

X = generator(1000000)

remaining_amount = next(X)
print(f"Остаток ипотеки: {remaining_amount} рублей")

while remaining_amount >= 0:
    payment_amount = float(input("Введите сумму для погашения кредита: "))
    remaining_loan = X.send(payment_amount)
    print(f"Остаток ипотеки: {remaining_loan} рублей")