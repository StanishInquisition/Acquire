""" for testing alt board functions, getting the row/column labels in, etc."""
import pprint

pp = pprint.PrettyPrinter(width=100, compact=True)

rows = ['A', 'B', 'C',
        'D', 'E', 'F',
        'G', 'H', 'I']
print(len(rows))
columns = ['@',
           '01', '02', '03',
           '04', '05', '06',
           '07', '08', '09',
           '10', '11', '12']
grid = [["[]"] * (len(columns) - 1) for x in range(len(rows))]
# creates a nested list the length of the number of columns desired
# then repeats as many times as the number of rows desired

# insert the strings from "rows" before each "row" (nested list),
# correlating with index of item in rows
for i in range(len(rows)):
    grid[i].insert(0, rows[i])

grid.insert(0, columns[:])
pp.pprint(grid)


# list.insert(i, x)
# Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).
#######################################
# list.index(x)
# Return the index in the list of the first item whose value is x.
# It is an error if there is no such item.

# for item in rows:
#      grid.insert(rows.index(item), "butts")
# for row in grid, item in rows:
#     i = 0
#     grid.insert(rows.index(item), rows[i])
#     i += 1
