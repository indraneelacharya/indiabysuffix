from geopy.geocoders import Nominatim
from PIL import Image, ImageDraw, ImageFont
import csv
import random
import colorsys
import time

loc = Nominatim(user_agent="GetLoc")

suffix_list = ['pur', 'puri', 'pura', 'pora', 'puram', 'gaon', 'gum', 'halli', 'palle', 'palli' 
'nagar', 'wadi', 'patti', 'abad','hari', 'khera', 'garh', 'guda', 'uru', 'oor']
suf_dict={}

colors_list = ['#ff0000','#ff8c00',
'#ffd700','#00ff00','#ba55d3','#00fa9a','#e9967a','#00ffff','#0000ff','#ff00ff','#1e90ff',
'#dda0dd','#ff1493','#87cefa','#fdf5e6',"#2f4f4f",'#2e8b57','#800000','#808000','#00008b']
a = suffix_list
left = 68.42
right = 97+(25/60)
top = 37+(6/60)
bottom = 8+(4/60)
width = right - left
height = top - bottom
pixel_width = 1130
pixel_height = 1250

global img 
img = Image.open("/Users/indraneelacharya/Documents/Py/INDIA/india_new.jpg")
global draw
draw = ImageDraw.Draw(img)

def legend():
    i = 0
    for key,val in suf_dict.items():     
        hex = val
        font = ImageFont.truetype('/Users/indraneelacharya/Documents/Py/INDIA/Open_Sans/static/OpenSans/OpenSans-SemiBold.ttf', 10) 
        x = ((i)//200)*60
        y = i%200
        rad = 5
        leftUpPoint = (x-rad+20, y-rad+20)
        rightDownPoint = (x+rad+20, y+rad+20)
        twoPointList = [leftUpPoint, rightDownPoint]
        draw.ellipse(twoPointList, fill=hex)
        text = key
        draw.text((x-rad+40, y-rad+18), text, fill ="black", font = font, align ="left") 
        i+=20

with open('/Users/indraneelacharya/Documents/Py/INDIA/cities.csv', mode ='r',encoding = 'unicode_escape') as file:
    csvFile = csv.reader(file)
    i = 1
    j = 1
    colors_num = 0
    for lines in csvFile:
        if lines != None:
            j+=1
            location = lines[0]
            state = lines[1]
            if ((location[-4:] in a) or (location[-3:] in a) or (location[-5:] in a)):
                if (location[-5:] in a):
                    suffix = location[-5:]

                elif (location[-4:] in a):
                    suffix = location[-4:]

                elif (location[-3:] in a):
                    suffix = location[-3:]


                if (suffix not in suf_dict):
                    '''h,s,l = random.random(), 0.5 + random.random()/2.0, 0.4 + random.random()/5.0
                    r,g,b = [int(256*i) for i in colorsys.hls_to_rgb(h,l,s)]   
                    suf_dict[suffix] = (r,g,b)'''
                    suf_dict[suffix] = colors_list[colors_num]
                    colors_num+=1
                    hex = colors_list[colors_num]
                else:
                    hex = suf_dict[suffix]
                
                try:
                    getLoc = loc.geocode(location +','+ state)
                except:
                    print()
                    continue
                if getLoc != None:
                    i+=1
                    
                    print(location,state,suffix,i)
                    pixels = img.load() # create the pixel map
                    lat = getLoc.latitude
                    long = getLoc.longitude
                    x = pixel_width*(long-left)/width + 15
                    y = pixel_height-pixel_height*(lat-bottom)/height
                    rad = 1
                    leftUpPoint = (x-rad, y-rad)
                    rightDownPoint = (x+rad, y+rad)
                    twoPointList = [leftUpPoint, rightDownPoint]
                    draw.ellipse(twoPointList, fill=(hex))
                    i+=1
                    if j%100 ==0: 
                        
                    if j%1000 ==0:    
                        img.show()

legend()
img.save("/Users/indraneelacharya/Documents/Py/INDIA/india_new2.jpg")
img.show()

