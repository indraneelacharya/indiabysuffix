import csv
with open('/Users/indraneelacharya/Documents/Py/INDIA/data.csv', mode ='r',encoding = 'unicode_escape'

) as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        print(lines)