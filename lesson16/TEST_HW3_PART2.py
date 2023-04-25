customers = [
    dict(id=1, total=200, coupon_code='F20'),  # F20: fixed, $20
    dict(id=2, total=150, coupon_code='P30'),  # P30: percent, 30%
    dict(id=3, total=100, coupon_code='P50'),  # P50: percent, 50%
    dict(id=4, total=110, coupon_code='F15'),  # F15: fixed, $15
]

for customer in customers:
    
    if customer ['coupon_code'] =='F20':
        customer['Discount'] = 20    
    if customer ['coupon_code'] =='P30':
        customer['Discount'] = customer['total']*0.30    
    if customer ['coupon_code'] =='P50':
        customer['Discount'] =  customer['total']*0.50
    if customer ['coupon_code'] =='F15':
        customer['Discount'] = 15

    for customer in customers:
        print(str(customer['id']) + ' '+ str(customer['total']) + ' $'+ str(customer['Discount']))
    #if customer['coupon_code'] =='F20':
        #print (str(csutomer['id']) + ' ' + str(customer['total'])+' $'+str(customer['Discount']))
    
   # if customer ['coupon_code'] =='P30':
      #  print (str (customer['id']) +' '+str (customer ['total']) +' $'+ str(['total]*0.30))
                
   # if customer ['coupon_code'] =='P50':
       # print (str (customer['id']) +' '+str (customer ['total']) +' $'+ str(['total]*0.50))
                
   # if customer ['coupon_code'] =='F15':
       # print (str (customer['id']) +' '+str (customer ['total']) + str(['total'])*'$15'))

            
