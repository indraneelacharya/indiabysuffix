import geonamescache
import csv


gc = geonamescache.GeonamesCache()
countries = gc.get_cities()
# print countries dictionary
with open("a.csv", mode = 'w') as f:
    wr = csv.writer(f)
    for c in countries.values():
        if c['countrycode'] == 'IN':
            print(c['name'])
            wr.write(c['name'])
    #for c in countries:
 #   print(c)
# you really wanna do something more useful with the data...