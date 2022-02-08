import requests
import bs4
import string
import pandas as pd
from IPython.display import Image, HTML
import shutil
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

def main():
	os.mkdir("C:\\Users\\Duncan\\Web-scraped_Images") #create new directory
	url_base = "https://archive.tfljamcams.net/"
	html_page = requests.get(url_base) 
	soup = bs4.BeautifulSoup(html_page.content, 'html.parser') #extract html from url
	FINDALL_LI = soup.find_all('li') #find all txt corresponding to locations
	location_list = []
	for x in FINDALL_LI:
	    location_list.append(str(x).partition(":")[0][4:-1]) #save locations as a list
	for j in range(0,3): #replace 3 with len(location_list) in full version
	    print(j) #print to console to check it's working
	    url_location_ext = location_list[j]
	    print("url_location_ext : " + url_location_ext) #print to console to check it's working
	    os.mkdir("C:\\Users\\Duncan\\Web-scraped_Images\\" + url_location_ext) #create new directory
	    url_location = url_base + "archive/" + url_location_ext + "/" #new url per location
	    print("url_location : " + url_location) #print to compare the difference
	    html_page = requests.get(url_location)
	    soup = bs4.BeautifulSoup(html_page.content, 'html.parser') #extract html from url
	    FINDALL_TD = soup.find_all('td') #find all txt corresponding to dates
	    date_list = []
	    for x in FINDALL_TD:
	        date_list.append(str(x).partition("/")[2][:10]) #save dates as a list
	    for k in range(0,3): #replace 3 with len(date_list) in full version
	        url_date_ext = date_list[k]
	        print("url_date_ext : " + url_date_ext) #print to console to check it's working
	        os.mkdir("C:\\Users\\Duncan\\Web-scraped_Images\\"+ url_location_ext +"\\" + url_date_ext) #create new directory
	        url_location_and_date = url_location + url_date_ext + "/"
	        print(url_location_and_date) #print to console to check it's working
	        html_page = requests.get(url_location_and_date)
	        soup = bs4.BeautifulSoup(html_page.content, 'html.parser')
	        for i in range(0,3): #replace 3 with len(soup.select('.magnify')) in full version
	            #only takes all images from today therefore max is 240 
	            example = soup.select('.magnify')[i].attrs['src']
	            print(example)
	            example_filepath = "C:\\Users\\Duncan\\Web-scraped_Images\\" + url_location_ext + "\\" + url_date_ext + "\\" + example
	            final_url = url_location_and_date + example
	            r = requests.get(final_url, stream=True) #Get request on full_url
	            if r.status_code == 200: #200 status code = OK
	               with open(example_filepath, 'wb') as f: 
	                  r.raw.decode_content = True
	                  shutil.copyfileobj(r.raw, f)
	                  print(final_url)
	return

if__name__ == "__main__":
	main()
