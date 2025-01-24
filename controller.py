#PARSE INPUT
#SETUP_SEARCH((site, keywords)) -->
#   SCRAPPER(search, loop, extract) --> RETURN DATA
#   DATA_TREATMENT(DATA) --> SQL & CSV
#SETUP_REPORT
#SETUP_EXPORT

from interface import test_data, test_search
from scrapper import Website_Scrapper, Content_Cleaner

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

def run_search(keyword, website_search):
    links = []
    content = []
    pattern = website_search.kw_pattern_maker(keyword)
    page = website_search.search_kw(pattern)
    while page:
        links.append(website_search.get_links(page))
        content.append(website_search.extract_links_content(links))
        page = website_search.update_page(page)
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
        content = run_search(kw, search[i])
        if search[i].id == 0:
            cleaner = Content_Cleaner("padrao",0)
        elif search[i].id == 1:
            pass
        else:
            print("error, no scrapper ID associated with ", i)
        extract_content(cleaner,content)