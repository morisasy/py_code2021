# Merge duplicate blocks in condition

def prop_payment(payment, currency):
    if currency == "USD":
        process_standard_payment(payment)
    elif currency == "EUR":
        process_standard_payment(payment)

    else:
        process_standard_payment(payment)

def process_payment(payment, currency):
       if  currency == "USD" or currency == "EUR":
           process_standard_payment(payment)
       else:
           process_standard_payment(payment)
#