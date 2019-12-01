import csv

f = open("books.csv")
reader = csv.reader(f)

length = [0, 0, 0, 0]

for row in reader:
    for i in range(4):
        if length[i] < len(row[i]):
            length[i] = len(row[i])
            print(row[i])

print(length)