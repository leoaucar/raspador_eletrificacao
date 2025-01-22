import requests
from bs4 import BeautifulSoup

class Website_Scrapper:
    def __init__(self,website,url,id):
        self.website = website
        self.url = url
        self.id = id
    
    # This will change in inheritance
    def search_kw(self, keywords):
        pass

    def get_links(self, page):
        pass

    def next_page(self, page):
        pass

    def scroll_page(self, page):
        return page
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