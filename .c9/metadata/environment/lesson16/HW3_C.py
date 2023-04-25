{"filter":false,"title":"HW3_C.py","tooltip":"/lesson16/HW3_C.py","undoManager":{"mark":6,"position":6,"stack":[[{"start":{"row":0,"column":0},"end":{"row":25,"column":0},"action":"insert","lines":["import csv","","# create empty lists for each column","b_list = []","e_list = []","f_list = []","g_list = []","i_list = []","","# read the CSV file and append the values to the corresponding lists","with open('customer_data.csv', newline='') as csvfile:","    reader = csv.reader(csvfile)","    for row in reader:","        b_list.append(row[1])","        e_list.append(row[3])","        f_list.append(row[2])","        g_list.append(row[4])","        i_list.append(row[0])","","# zip the lists together","zipped_lists = zip(b_list, e_list, f_list, g_list, i_list)","","# display the zipped lists row by row using a for loop","for row in zipped_lists:","    print(row)",""],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":25,"column":0},"action":"remove","lines":["import csv","","# create empty lists for each column","b_list = []","e_list = []","f_list = []","g_list = []","i_list = []","","# read the CSV file and append the values to the corresponding lists","with open('customer_data.csv', newline='') as csvfile:","    reader = csv.reader(csvfile)","    for row in reader:","        b_list.append(row[1])","        e_list.append(row[3])","        f_list.append(row[2])","        g_list.append(row[4])","        i_list.append(row[0])","","# zip the lists together","zipped_lists = zip(b_list, e_list, f_list, g_list, i_list)","","# display the zipped lists row by row using a for loop","for row in zipped_lists:","    print(row)",""],"id":2},{"start":{"row":0,"column":0},"end":{"row":21,"column":0},"action":"insert","lines":["customers = [","    dict(id=1, total=200, coupon_code='F20'),  # F20: fixed, $20","    dict(id=2, total=150, coupon_code='P30'),  # P30: percent, 30%","    dict(id=3, total=100, coupon_code='P50'),  # P50: percent, 50%","    dict(id=4, total=110, coupon_code='F15'),  # F15: fixed, $15","]","","for customer in customers:","    coupon_code = customer['coupon_code']","    total = customer['total']","","    if coupon_code.startswith('F'):","        # apply fixed discount","        discount = float(coupon_code[1:])","        total -= discount","    elif coupon_code.startswith('P'):","        # apply percent discount","        discount = float(coupon_code[1:]) / 100.0 * total","        total -= discount","","    print(f\"Customer {customer['id']} has a discount of ${discount:.2f} applied, and their new total is ${total:.2f}\")",""]}],[{"start":{"row":12,"column":10},"end":{"row":12,"column":30},"action":"remove","lines":["apply fixed discount"],"id":3},{"start":{"row":12,"column":10},"end":{"row":12,"column":28},"action":"insert","lines":["use a set discount"]}],[{"start":{"row":16,"column":10},"end":{"row":16,"column":32},"action":"remove","lines":["apply percent discount"],"id":4},{"start":{"row":16,"column":10},"end":{"row":16,"column":30},"action":"insert","lines":["put a percentage off"]}],[{"start":{"row":20,"column":72},"end":{"row":20,"column":100},"action":"remove","lines":["applied, and their new total"],"id":5},{"start":{"row":20,"column":72},"end":{"row":20,"column":101},"action":"insert","lines":["used, and their updated total"]}],[{"start":{"row":20,"column":38},"end":{"row":20,"column":41},"action":"remove","lines":["has"],"id":6},{"start":{"row":20,"column":38},"end":{"row":20,"column":39},"action":"insert","lines":["a"]},{"start":{"row":20,"column":39},"end":{"row":20,"column":40},"action":"insert","lines":["p"]},{"start":{"row":20,"column":40},"end":{"row":20,"column":41},"action":"insert","lines":["p"]},{"start":{"row":20,"column":41},"end":{"row":20,"column":42},"action":"insert","lines":["l"]},{"start":{"row":20,"column":42},"end":{"row":20,"column":43},"action":"insert","lines":["y"]}],[{"start":{"row":15,"column":37},"end":{"row":15,"column":38},"action":"insert","lines":[" "],"id":7}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":15,"column":38},"end":{"row":15,"column":38},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":1,"state":"start","mode":"ace/mode/python"}},"timestamp":1680016946669,"hash":"a81ddeec65633a5b89a0eecd4bdd744273657857"}