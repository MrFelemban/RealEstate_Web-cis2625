Customers
# create empty lists for each column
b_list = []
e_list = []
f_list = []
g_list = []
i_list = []

# read the CSV file and append the values to the corresponding lists
    for row in :
        b_list.append(row[1])
        e_list.append(row[3])
        f_list.append(row[2])
        g_list.append(row[4])
        i_list.append(row[0])

# zip the lists together
zipped_lists = zip(b_list, e_list, f_list, g_list, i_list)

# display the zipped lists row by row using a for loop
for row in zipped_lists:
    print(row)
