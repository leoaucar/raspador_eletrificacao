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
        if i['scrapper_id'] == 0:
            website = i['name']
            url = i['url']
            search[i['name']+'_scrapper'] = Website_Scrapper(website,url,0)
        elif i['scrapper_id'] == 1:
            pass
        else:
            print("error, no scrapper ID associated with ", i)
            break
    return search

def run_search(keywords):
    pass

def report_search():
    pass

search = setup_search(test_data, test_search)
for i in search:
    print(search[i].id)