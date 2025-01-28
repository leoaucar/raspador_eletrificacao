#PARSE INPUT
#SETUP_SEARCH((site, keywords)) -->
#   SCRAPPER(search, loop, extract) --> RETURN DATA
#   DATA_TREATMENT(DATA) --> SQL & CSV
#SETUP_REPORT
#SETUP_EXPORT

from interface import test_data, test_search
from scrapper import Website_Scrapper, Content_Cleaner
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

#para selenium
firefox_options = Options()
firefox_options.add_argument("--headless") # Run in headless mode
firefox_options.add_argument("--disable-gpu") 

def setup_search(sites):
    search = {}
    for i in sites:
        website = i['name']
        url = i['url']
        if i['scrapper_id'] == 0:
            search[i['name']+'_scrapper'] = Website_Scrapper(website,url,0)
        elif i['scrapper_id'] == 1:
            pass
        else:
            print("error, no scrapper ID associated with ", i['name'])
            break
    return search

def run_search(keyword, website_search,firefox_options):
    links = []
    content = []
    current_page = 1
    pattern = website_search.kw_pattern_maker(keyword)
    page = website_search.search_kw(pattern, current_page,firefox_options)
    while page:
        new_links = website_search.get_links(page)
        links.extend(new_links)
        if len(new_links) == 0:
            break
        page, current_page = website_search.next_page(keyword, current_page,firefox_options)
    content = website_search.extract_links_content(links, firefox_options)

    return content

def extract_content(cleaner, content):
    processed_html = cleaner.process_html(content)
    text = cleaner.extract_text(processed_html)
    author = cleaner.extract_author(processed_html)
    date = cleaner.extract_date(processed_html)
    #images = cleaner.extract_images(processed_html)
    cleaner.save_sql(text,author,date)
    cleaner.save_csv(text,author,date)

def report_search():
    pass

#realiza as buscas para cada caso (IRA VIRAR FUNÇÂO QUANDO INTEGRAR COM INTERFACE)
keywords = test_search
search = setup_search(test_data)
for i in search:
    for kw in keywords:
        content = run_search(kw, search[i],firefox_options)
        if search[i].id == 0:
            cleaner = Content_Cleaner("padrao",0)
        elif search[i].id == 1:
            pass
        else:
            print("error, no scrapper ID associated with ", i)
        extract_content(cleaner,content)