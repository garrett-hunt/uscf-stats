import requests
from bs4 import BeautifulSoup

def get_page_count(soup):
    pagination = soup.find_all('nobr')
    if pagination:
        pageCount = len(pagination)
    else:
        pageCount = 1
    return pageCount

def is_not_nbsp(value):
    return value != '\xa0'

def is_online(value):
    return 'ONL:' in value

def get_page_data(soup, classical_results, quick_results, blitz_results):
    rows = soup.find_all('tr', bgcolor=['FFFFC0', 'FFFF80'])
    
    for row in rows:
        cells = row.find_all('td', width='160')
        
        if len(cells) >= 3:
            classical_cell = cells[0].text
            if is_not_nbsp(classical_cell):
                if not is_online(classical_cell):
                    classical_results.append(classical_cell)
                else:
                    online_classical_results.append(classical_cell)

            quick_cell = cells[1].text
            if is_not_nbsp(quick_cell):
                if not is_online(quick_cell):
                    quick_results.append(quick_cell)
                else:
                    online_quick_results.append(quick_cell)

            blitz_cell = cells[2].text
            if is_not_nbsp(blitz_cell):
                if not is_online(blitz_cell):
                    blitz_results.append(blitz_cell)
                else:
                    online_blitz_results.append(blitz_cell)

classical_results = []
quick_results = []
blitz_results = []
online_classical_results = []
online_quick_results = []
online_blitz_results = []

uscf_id = '15437654'
base_url = f'https://www.uschess.org/msa/MbrDtlTnmtHst.php?{uscf_id}'
first_page_url = requests.get(base_url).text
soup = BeautifulSoup(first_page_url, 'lxml')

pageCount = get_page_count(soup)
get_page_data(soup, classical_results, quick_results, blitz_results)

for page in range(2, pageCount + 1):
    next_page_url = f'{base_url}.{page}'
    page_content = requests.get(next_page_url).text
    next_soup = BeautifulSoup(page_content, 'lxml')
    get_page_data(next_soup, classical_results, quick_results, blitz_results)

for i in classical_results:
    print(i)
