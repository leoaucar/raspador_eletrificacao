import requests
from bs4 import BeautifulSoup

class Website_Scrapper:
    def __init__(self,website,url,id):
        self.website = website
        self.url = url
        self.id = id
    
    # This will change in inheritance
    def search_kw():
        pass

    def get_links():
        pass

    def next_page():
        pass

    def scroll_page():
        pass
    # Changing block ends here

    def extract_link_content():
        pass

class Content_Cleaner:
    def __init__(self,website):
        self.website

    def process_html(content):
        pass

# This will change in inheritance
    def extract_text(content):
        pass
    def extract_author(content):
        pass
    def extract_date(content):
        pass
    def extract_images(content):
        pass
# Changing block ends here

    def save_csv():
        pass
    def save_sql():
        pass