lst1 = [10, 20, 45, 60, 55, 48]
lst2 = [20, 35, 40, 55, 60, 70]
lst3 = [35, 40, 60, 85, 78, 70]

union_list = []

for i in list1:
    if i not in union_list:
        union_list.append(i)

for i in list2:
    if i not in union_list:
        union_list.append(i)

for i in list3:
    if i not in union_list:
        union_list.append(i)

print(union_list)