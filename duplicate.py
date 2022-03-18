dictionary=[1,2,2,1,5,6,4,8,5]

duplicateitem = set()
uniqueitem = []
for x in dictionary:
    if x not in duplicateitem:
        uniqueitem.append(x)
        duplicateitem.add(x)

print(duplicateitem)