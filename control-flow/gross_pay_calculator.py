def computepay(hrs, rate):
    if hrs <= 40:
        pay = hrs * rate
    else:
        pay = (40 * rate) + (hrs - 40) * rate * 1.5
    return pay

hrs = input("Enter Hours:")
hrs = float(hrs)
rate = input("Enter Rate:")
rate = float(rate)
p = computepay(hrs, rate)
print("Pay", p)