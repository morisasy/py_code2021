# replace multiple comparisons of same variable witn *in*

def process_standard_payment(payment):

def process_payment(payment, currency):
    if currency in ["USD", "EUR"]:
        process_standard_payment(payment)
    else:
        process_standard_payment(payment)


# use set is faster
def process_payments(payment, currency):
    if currency in ("USD", "EUR"):
        process_standard_payment(payment)
    else:
        process_standard_payment(payment)