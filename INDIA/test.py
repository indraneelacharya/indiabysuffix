import random
from PIL import Image, ImageDraw
from geopy.geocoders import Nominatim
from PIL import Image
import csv

# calling the Nominatim tool
loc = Nominatim(user_agent="GetLoc")

img =Image.open("/Users/indraneelacharya/Documents/Py/INDIA/india_new.jpg")
draw = ImageDraw.Draw(img)
getLoc = loc.geocode("kanyakumari")
lat = getLoc.latitude
long = getLoc.longitude

left = 68+(7/60)
right = 97+(25/60)
top = 37+(6/60)
bottom = 8+(4/60)
width = right - left
height = top - bottom

print(lat,long)

pixel_width = 1130
pixel_height = 1250

x = pixel_width*(long-left)/width + 15
y = pixel_height-pixel_height*(lat-bottom)/height
r = 0.5
leftUpPoint = (x-r, y-r)
rightDownPoint = (x+r, y+r)
twoPointList = [leftUpPoint, rightDownPoint]
draw.ellipse(twoPointList, fill="red")

#draw.point((pixel_width/(lat-left),(pixel_height/(long-bottom))), fill="red")
#draw.ellipse((pixel_width/(lat-left), pixel_width/(lat-left), (pixel_height/(long-bottom)), (pixel_height/(long-bottom))), fill = 'blue', outline ='blue')


img.show()
#img.save("/Users/indraneelacharya/Documents/Py/INDIA/india3.jpeg")
