import csv

data = []

file = open("dataset_2.csv", "r")

csvreader = csv.reader(file)

for row in csvreader:
    data.append(row)

headers = data[0]

planet_data = data[1:]

for datapoint in planet_data:
    datapoint[2] = datapoint[2].lower()

planet_data.sort(key = lambda planet_data : planet_data[2])
file2 = open("dataset_2_sorted.csv", "a+")
csvwriter = csv.writer(file2)
csvwriter.writerow(headers)
csvwriter.writerows(planet_data)
