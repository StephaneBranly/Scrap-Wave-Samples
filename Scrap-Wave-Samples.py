# import libraries
import urllib.request
import numpy as np
import sys
from bs4 import BeautifulSoup

import requests

for i in range(1,210):
    
    # specify the url
    quote_page = 'https://freewavesamples.com/?page='+str(i)

    # query the website and return the html to the variable ‘page’
    page = urllib.request.urlopen(quote_page)

    # parse the html using beautiful soup and store in variable `soup`
    soup = BeautifulSoup(page, 'html.parser')

    # Take out the <div> of name and get its value
    samples_page = soup.find_all('div', attrs={'class': 'sample'})


    for wave_sample in samples_page:
        wave_sample = wave_sample.find('a')
        wave_sample = wave_sample.text.strip() # strip() is used to remove starting and trailing
        wave_sample=wave_sample.replace(" ", "-")
        wave_sample=wave_sample.replace(".", "-")
        print (wave_sample)
        
        url_sample = 'https://freewavesamples.com/files/'+wave_sample+'.wav'
        r = requests.get(url_sample, allow_redirects=True)
        if(r.status_code == 200):
            open('freewavessamples/'+wave_sample+'.wav', 'wb').write(r.content)

