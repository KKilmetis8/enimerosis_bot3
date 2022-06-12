from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

# ora 'https://www.gazzetta.gr/protoselida/athlitikes-efimerides/ora-ton-sport'
def eikona_ora(url):
    # URL oras
    url_ora = url
    
    req = Request(url_ora, headers={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0"})
    webpage = urlopen(req).read()
    
    page_soup = soup(webpage, "html.parser")
    images = page_soup.find_all('img')
      
    for item in images:
        if 'newspapers' in item['src']:
            url_eikonas = item['src']
            url_eikonas = 'https://www.gazzetta.gr' + url_eikonas
    return url_eikonas