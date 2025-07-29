
# Scraping MFN: Stockholm large, mid and small cap

import requests
from bs4 import BeautifulSoup

link_all = 'https://mfn.se/all/s/nordic?filter=(and(or(.properties.lang%3D%22en%22))(or(a.market_segment_ids%40%3E%5B13%5D)(a.market_segment_ids%40%3E%5B14%5D)(a.market_segment_ids%40%3E%5B15%5D)))'
link_large = 'https://mfn.se/all/s/nordic?filter=(and(or(.properties.lang%3D%22en%22))(or(a.market_segment_ids%40%3E%5B13%5D)))'
link_mid = 'https://mfn.se/all/s/nordic?filter=(and(or(.properties.lang%3D%22en%22))(or(a.market_segment_ids%40%3E%5B14%5D)))'
link_small = 'https://mfn.se/all/s/nordic?filter=(and(or(.properties.lang%3D%22en%22))(or(a.market_segment_ids%40%3E%5B15%5D)))'

def get_pdf(link: str) -> tuple[str, str]:
    """
    Extracts latest company pdf on MFN website if exists. 

    Args:
        link (str): URL to MFN website to scrape. 

    Returns:
        tuple[str, str]: returns pdf for reports and pdf_any for all types of attached pdf:s if they exist. 
        Otherwise 'No PDF available' and 'No pdf:s available' is returned.
    """
    response = requests.get(link)

    soup = BeautifulSoup(response.text, 'html.parser')
    box = soup.find('div', class_='short-item compressible')
    
    url = find_pdf(box)
    url_any = find_any_pdf(box)

    if url != 'No PDF available':
        pdf = download_pdf(url)
    elif url == 'No PDF available':
        pdf = url
    
    if url_any != 'No pdf:s available':
        pdf_any = download_pdf(url)
    elif url_any == 'No pdf:s available':
        pdf_any = url_any

    return pdf, pdf_any

def find_pdf(box) -> str:
    """
    Extracts latest URL for pdf:s with title='PDF'.

    Args:
        box (bs4.element.Tag): element in HTML from BeautifulSoup

    Returns:
        str: URL to PDF if exists, otherwise 'No PDF available'
    """

    try:
        link_pdf = box.find('a', class_='attachment-icon', title='PDF')['href']
        return link_pdf
    except:
        return 'No PDF available'
    
def find_any_pdf(box) -> str:
    """
    Extracts latest URL for pdf:s with any title.

    Args:
        box (bs4.element.Tag): element in HTML from BeautifulSoup

    Returns:
        str: URL to PDF if exists, otherwise 'No pdf:s available'
    """

    try:
        link_pdf = box.find('a', class_='attachment-icon')['href']
        return link_pdf
    except:
        return 'No pdf:s available'

def pdf_to_str(link) -> str:
    return text 

if __name__=='__main__':
    pdf = get_pdf(link_small)
    