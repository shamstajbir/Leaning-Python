# i) list:
The_list = [1, 2, 3, 4, 5]
print("list:", The_list)

# ii) len:
print("len:", len(The_list))

# iii) count:
print(" count :", The_list.count(3))

# iv) index:
print("The index of the list:", The_list.index(4))

# v) append:
The_list.append(6)
print("The appended list:", The_list)

# vi) insert:
The_list.insert(3, 9)
print("The insert of the list:", The_list)

# vii) extend():
The_list.extend([15, 12, 11])
print("The extend of the list:", The_list)

# viii) remove:
The_list.remove(5)
print("The removal of the list:", The_list)

# ix) pop:
popped_item = The_list.pop()
print("pop:", popped_item)
print("After pop of the list:", The_list)

# x) reverse:
The_list.reverse()
print("The reverse of the list:", The_list)

# xi) sort:
The_list.sort()
print("The sort of the list:", The_list)

# xii) copy:
The_list_copy = The_list.copy()
print("The copy of the list:",The_list_copy)
