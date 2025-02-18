# import calendar
# year, month = int(input("Year: ")), int(input("Month: "))
# print(calendar.TextCalendar().formatmonth(year, month))
# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 9, 10}
are_disjoint = set1.isdisjoint(set2)

if are_disjoint:
    print("The sets are disjoint, they have no common elements.")




else:
    print("The sets are not disjoint, they have common elements.")
