# mortgage.py
#
# Exercise 1.7

extra_payment_start_month = int(input("extra start month: "))
extra_payment_end_month = int(input("extra end month: "))
extra_payment = int(input("extra payment: "))
principal = 500000.0
rate = 0.05
payment_original = 2684.11
total_paid = 0.0
payment_increased=2684.11+extra_payment
months=1
payment=0

while principal > 0:
    if months>=extra_payment_start_month and months <=extra_payment_end_month:
        payment=payment_increased
        
    else:
        payment=payment_original

    principal = principal * (1+rate/12) - payment
    if principal<0:
        total_paid=total_paid+ payment-abs(principal)
        principal=0.00

    else:
        total_paid = total_paid + payment


    print(f"{months},{total_paid:0.2f}{principal:0.2f}")

    months=months+1



    

print(f'Total paid{total_paid:.2f}')
print(f'Months{months}')