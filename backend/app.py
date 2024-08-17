from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/api/id")
def id():
    return get_id(soup)

@app.route("/api/name")
def name():
    return get_name(soup)

# @app.route("/api/id")
# def id():
#     result = get_id(soup)
#     return result

# @app.route("/api/id")
# def id():
#     result = get_id(soup)
#     return result

# @app.route("/api/id")
# def id():
#     result = get_id(soup)
#     return result

# @app.route("/api/id")
# def id():
#     result = get_id(soup)
#     return result

def get_id(soup):
    id_cell = soup.find('font')
    if id_cell:
        id = id_cell.get_text()[0:8]
        return id
    return None

def get_name(soup):
    name_cell = soup.find('font')
    if name_cell:
        name = name_cell.get_text()[10:]
        return jsonify({"name": name})
    return None

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

def get_column_data(soup, column_results, online_column_results, column_index):
    rows = soup.find_all('tr', bgcolor=['FFFFC0', 'FFFF80'])
    
    for row in rows:
        cells = row.find_all('td', width='160')
        if cells:
            cell_result = cells[column_index].text
            if is_not_nbsp(cell_result):
                if not is_online(cell_result):
                    column_results.append(cell_result)
                else:
                    online_column_results.append(cell_result)

classical_results = []
quick_results = []
blitz_results = []
online_classical_results = []
online_quick_results = []
online_blitz_results = []

def get_page_data(soup, classical_results, quick_results, blitz_results, online_classical_results, online_quick_results, online_blitz_results):
    get_column_data(soup, classical_results, online_classical_results, 0)
    get_column_data(soup, quick_results, online_quick_results, 1)
    get_column_data(soup, blitz_results, online_blitz_results, 2)


id = '12743305'
base_url = f'https://www.uschess.org/msa/MbrDtlTnmtHst.php?{id}'
first_page_url = requests.get(base_url).text
soup = BeautifulSoup(first_page_url, 'lxml')

pageCount = get_page_count(soup)
get_page_data(soup, classical_results, quick_results, blitz_results, online_classical_results, online_quick_results, online_blitz_results)

for page in range(2, pageCount + 1):
    next_page_url = f'{base_url}.{page}'
    page_content = requests.get(next_page_url).text
    next_soup = BeautifulSoup(page_content, 'lxml')
    get_page_data(next_soup, classical_results, quick_results, blitz_results, online_classical_results, online_quick_results, online_blitz_results)

if __name__ == "__app__":
    app.run(debug=True)