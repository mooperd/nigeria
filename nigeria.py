
import csv

with open('nga_pop_sendist_2016.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if int(row["Population2016"]) < 1000000:
            print(row["admin1Name_en"], row ['Population2016'])


