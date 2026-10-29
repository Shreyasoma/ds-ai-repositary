FILE_PATH = "datasets/chai_sales.csv"

with open(FILE_PATH, "r", encoding="utf-8") as file:
    lines = file.readlines()

# TODO 1: print the header line (the first line of the file)
header_line = lines[0]
print(header_line)

# TODO 2: print the number of DATA rows (not counting the header)
data_rows = lines[1:]
print(len(data_rows))

# TODO 3: print the first three DATA rows, each split into a list of values
for line in lines[1:4]:
    print(line.strip().split(","))

first_row = lines[1].strip().split(",")
cups_sold = first_row[1]
print(cups_sold)
print(int(cups_sold) + 1)
print(type(cups_sold))