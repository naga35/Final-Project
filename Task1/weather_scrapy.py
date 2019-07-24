import urllib.request
from bs4 import BeautifulSoup

def get_all_links_from_web_page(url):
    html_links = []
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    base_url = "https://karki23.github.io/Weather-Data/"
    for link in soup.findAll('a'):
        html_file = link.get('href')
        url = base_url + "/" + html_file
        html_links.append(url)
    return html_links

def get_tabular_data_from_web_page(url):
    data = urllib.request.urlopen(url)
    html = data.read()
    soup = BeautifulSoup(html, 'html.parser')
    trs = soup.find_all('tr')
    rows = [[td.text for td in tr.find_all('td')] for tr in trs]
    return rows
