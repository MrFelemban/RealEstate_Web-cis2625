customers = [
    dict(id=1, total=200, coupon_code='F20'),  # F20: fixed, $20
    dict(id=2, total=150, coupon_code='P30'),  # P30: percent, 30%
    dict(id=3, total=100, coupon_code='P50'),  # P50: percent, 50%
    dict(id=4, total=110, coupon_code='F15'),  # F15: fixed, $15
]

def customer_discount1 (c_list):
    for customer in c_list:

        if customer ['coupon_code'] = ='F20':
            print (str (customer['id']) +' '+str (customer ['total']) + ' $20')
    
        if customer ['coupon_code'] = ='P30':
            print (str (customer['id']) +' '+str (customer ['total']) +' $'+ str(['total]*0.30))
                
        if customer ['coupon_code'] = ='P50':
            print (str (customer['id']) +' '+str (customer ['total']) +' $'+ str(['total]*0.50))
                
        if customer ['coupon_code'] = ='F15':
            print (str (customer['id']) +' '+str (customer ['total']) + ' $15')
            
def customer_discount2(cust_list):
    
customer_discount1(customers)


            
