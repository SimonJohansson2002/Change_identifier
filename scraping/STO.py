
# Scraping MFN: Stockholm large, mid and small cap

import requests
from bs4 import BeautifulSoup

link_all = 'https://mfn.se/all/s/nordic?filter=(and(or(.properties.lang%3D%22en%22))(or(a.market_segment_ids%40%3E%5B13%5D)(a.market_segment_ids%40%3E%5B14%5D)(a.market_segment_ids%40%3E%5B15%5D)))'
link_large = 'https://mfn.se/all/s/nordic?filter=(and(or(.properties.lang%3D%22en%22))(or(a.market_segment_ids%40%3E%5B13%5D)))'
link_mid = 'https://mfn.se/all/s/nordic?filter=(and(or(.properties.lang%3D%22en%22))(or(a.market_segment_ids%40%3E%5B14%5D)))'
link_small = 'https://mfn.se/all/s/nordic?filter=(and(or(.properties.lang%3D%22en%22))(or(a.market_segment_ids%40%3E%5B15%5D)))'

def find_pdf(link: str):
    #Find link to pdf
    response = requests.get(link)

    soup = BeautifulSoup(response.text, 'html.parser')
    box = soup.find('div', class_='short-item compressible') #'short-item-wrapper grid-u-1 grid-u-md-1-2 grid-u-lg-1-3 grid-u-xl-1-4 removable-grid'
    
    try:
        link_pdf = box.find('a', class_='attachment-icon', title='PDF')['href']
    except:
        return 'No pdf available'
    

    print(link_pdf)

    pdf = download_pdf(link)
    return pdf

def download_pdf(link):
    pass

if __name__=='__main__':
    pdf = find_pdf(link_large)
    