import csv
with open('/Users/indraneelacharya/Documents/Py/INDIA/cities.csv', mode ='r',encoding = 'unicode_escape') as file:
    csvFile = csv.reader(file)
    for line in csvFile:
        print(line[0])