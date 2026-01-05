def name_list(list1):
    for i in list1:
        yield i
for j in name_list(["subha","shree"]):
    print(j)