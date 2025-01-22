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

def run_search(keywords, website_search):
    content = []
    search_results = website_search.search_kw(keywords)
    links = []
    links.append(website_search.get_links(search_results))
    content.append(website_search.extract_links_content(links))
    return content

def extract_content(cleaner, content):
    cleaner.process_html(content)
    text = cleaner.extract_text(content)
    author = cleaner.extract_author(content)
    date = cleaner.extract_date(content)
    #images = cleaner.extract_images(content)
    cleaner.save_sql(text,author,date)
    cleaner.save_csv(text,author,date)

def report_search():
    pass

#realiza as buscas para cada caso
keywords = test_search
search = setup_search(test_data)
for i in search:
    content = run_search(keywords, search[i])
    if search[i].id == 0:
       cleaner = Content_Cleaner("padrao",0)
    elif search[i].id == 1:
        pass
    else:
        print("error, no scrapper ID associated with ", i)
    extract_content(cleaner,content)