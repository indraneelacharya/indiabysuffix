
#India By Suffix

Based on this project I discovered on [Twitter](https://twitter.com/stats_of_india/status/1575057780750569473). 
The idea was to map all the different places in India with common suffixes such as -pur, -abad, etc.
The following is a sample image that came up with preliminary data.

![Final Mapped Image.](https://github.com/indraneelacharya/indiabysuffix/blob/main/INDIA/india_new2.jpg)

The hardest part of the project was sourcing the information.
1) First source was a dataset of cities and towns that I discovered on kaggle which gave me around 4000 names, 
    which I knew was much lower than the true number but it was enough for a testrun of the program.
2) Second was a list from a census of India file that I discovered online.
3) Third source was by webscraping on this [website](https://www.citypopulation.de/en/india/). I scraped a 
    list of 7500 cities and their corresponding states. This helps acounts for places with the same name in 
    multiple states such as Aurangabad - Bihar, Maharashtra and Gujarat. 

Mapping the cities and towns on the image was the easy part, using the geocoders library I accessed the 
latitude and longitude and mapped those on the image using pixel width and height of the India map that 
I found on the internet. It is accurate within 5% in any direction of the accurate locations on the map.

Future modifications for the code - 
1) integrate pygame or similar library to create a user interface that can select certain suffixes to search
2) analyse the linguistic backgrounds of terms 
3) group similar suffixes such as (pur, pura, pora) which is more often a synactical difference in how they 
chose to spell it in english
