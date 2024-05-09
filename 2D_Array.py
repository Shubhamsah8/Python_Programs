# Take input for the number of rows and columns
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        # Take input for each element and append it to the current row
        element = int(input(f"Enter the element in ({i},{j}): "))
        row.append(element)

    matrix.append(row)

# Print the 2D array
for row in matrix:
    for element in row:
        print(element,end=" ")
    print()