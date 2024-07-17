def to_USA_dollar(currency):
    if currency == 0:
        return 0
    usd = currency * 0.012
    return usd

def to_EURO(currency):
    if currency == 0:
        return 0
    eur = currency * 0.011
    return eur

def to_YUAN(currency):
    if currency == 0:
        return 0
    yuan = currency * 0.087
    return yuan

currency = int(input("Enter Indian currency: "))

usd = to_USA_dollar(currency)
eur = to_EURO(currency)
yuan = to_YUAN(currency)

print(f"{currency} INR is {usd:.2f} USD")
print(f"{currency} INR is {eur:.2f} EUR")
print(f"{currency} INR is {yuan:.2f} CNY")
