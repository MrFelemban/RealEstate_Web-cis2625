customers = [
    dict(id=1, total=200, coupon_code='F20'),  # F20: fixed, $20
    dict(id=2, total=150, coupon_code='P30'),  # P30: percent, 30%
    dict(id=3, total=100, coupon_code='P50'),  # P50: percent, 50%
    dict(id=4, total=110, coupon_code='F15'),  # F15: fixed, $15
]

for customer in customers:
    coupon_code = customer['coupon_code']
    total = customer['total']

    if coupon_code.startswith('F'):
        # use a set discount
        discount = float(coupon_code[1:])
        total -= discount
    elif coupon_code.startswith('P'): 
        # put a percentage off
        discount = float(coupon_code[1:]) / 100.0 * total
        total -= discount

    print(f"Customer {customer['id']} apply a discount of ${discount:.2f} used, and their updated total is ${total:.2f}")
