import requests
from bs4 import BeautifulSoup

class Website_Scrapper:
    def __init__(self,website,url,id):
        self.website = website
        self.url = url
        self.id = id

    def kw_pattern_maker(self, keyword):
        keyword = keyword.replace(' ', '+')
        pattern = "busca/?palavra="+keyword
        return pattern
    
    # This will change in inheritance
    def search_kw(self, keyword_pattern):
        schema_url = "https://"
        r = requests.get(schema_url+self.url+'/'+keyword_pattern)
        page = r.text
        print(schema_url+self.url+'/'+keyword_pattern)
        return page

    def get_links(self, page):
        pass

    def update_page(self, page):
        pass

    # Changing block ends here

    def extract_links_content(self, links):
        pass

class Content_Cleaner:
    def __init__(self,website, id):
        self.website = website
        self.id = id

    def process_html(self, content):
        pass

# This will change in inheritance
    def extract_text(self, content):
        return
    def extract_author(self, content):
        pass
    def extract_date(self, content):
        pass
    def extract_images(self, content):
        pass
# Changing block ends here

    def save_csv(self, text,author,date):
        print("saved HTML:",text,author,date)
    def save_sql(self, text,author,date):
        print("saved csv:",text,author,date)