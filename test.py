import csv

# csv_reader = csv.reader(open("./rawData/test.csv"))
csv_reader = csv.reader(open("./rawData/Hokkaido.csv", 'r', encoding='UTF-8'))
i = 0
for row in csv_reader:
    # if i == 0:
    #     continue
    if i > 1:
        break
    print(row)
    i += 1