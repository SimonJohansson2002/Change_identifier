
# Scraping MFN: Stockholm large, mid and small cap

import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader
from io import BytesIO

link_all = 'https://mfn.se/all/s/nordic?filter=(and(or(.properties.lang%3D%22en%22))(or(a.market_segment_ids%40%3E%5B13%5D)(a.market_segment_ids%40%3E%5B14%5D)(a.market_segment_ids%40%3E%5B15%5D)))'
link_large = 'https://mfn.se/all/s/nordic?filter=(and(or(.properties.lang%3D%22en%22))(or(a.market_segment_ids%40%3E%5B13%5D)))'
link_mid = 'https://mfn.se/all/s/nordic?filter=(and(or(.properties.lang%3D%22en%22))(or(a.market_segment_ids%40%3E%5B14%5D)))'
link_small = 'https://mfn.se/all/s/nordic?filter=(and(or(.properties.lang%3D%22en%22))(or(a.market_segment_ids%40%3E%5B15%5D)))'
# Add links to industries later

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

def pdf_to_str(link: str) -> str:
    """
    Downloads a PDF from the given URL and extracts its text content.

    Args:
        link (str): URL to the PDF.

    Returns:
        str: Extracted text from the PDF.
    """

    try:
        response = requests.get(link)
        pdf_file = BytesIO(response.content)
        reader = PdfReader(pdf_file)

        text = ''
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

        return text.strip()
    
    except:
        return 'Error reading PDF'

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
        pdf = pdf_to_str(url)
    elif url == 'No PDF available':
        pdf = url
    
    if url_any != 'No pdf:s available':
        pdf_any = pdf_to_str(url_any)
    elif url_any == 'No pdf:s available':
        pdf_any = url_any

    return pdf, pdf_any

if __name__=='__main__':
    pdf, pdf_any = get_pdf(link_large)

    print(pdf)
    