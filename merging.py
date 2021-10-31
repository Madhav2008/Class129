import csv

dataset1 = []
dataset2 = []

file1 = open("final2.csv", "r")
csvreader = csv.reader(file1)

for row in csvreader:
    dataset1.append(row)

file2 = open("dataset_2_sorted.csv", "r")
csvreader = csv.reader(file2)

for row in csvreader:
    dataset2.append(row)

headers1 = dataset1[0]
planet_data1 = dataset1[1:]

headers2 = dataset2[0]
planet_data2 = dataset2[1:]

headers = headers1 + headers2
planet_data = []

for index, data_row in enumerate(planet_data1):
    planet_data.append(planet_data1[index] + planet_data2[index])

file = open("merged.csv", "a+")
csvwriter = csv.writer(file)
csvwriter.writerow(headers)
csvwriter.writerows(planet_data)