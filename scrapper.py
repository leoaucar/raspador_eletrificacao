import requests
from bs4 import BeautifulSoup
from selenium import webdriver


class Website_Scrapper:
    def __init__(self,website,url,id):
        self.website = website
        self.url = url
        self.id = id

    def kw_pattern_maker(self, keyword):
        keyword = keyword.replace(' ', '+')
        pattern = keyword
        return pattern
    
    # This will change in inheritance
    def search_kw(self, keyword_pattern, current_page, selenium_options):
        driver = webdriver.Firefox(selenium_options)
        schema_url = "https://"
        final_url = schema_url+self.url+'/page/'+ str(current_page) +'/?s='+keyword_pattern
        driver.get(final_url)
        page = driver.page_source
        driver.quit()
        print("searching",final_url)
        #r = requests.get(schema_url+self.url+'/page/'+ str(current_page) +'/?s='+keyword_pattern)
        #page = r.text
        return page

    def get_links(self, page):
        new_links = []
        soup = BeautifulSoup(page, "html.parser")
        for link in soup.find_all('h2'):
            new_links.append(link.find('a').get('href'))
        return new_links

    def update_page(self, page):
        pass

    def next_page(self, keyword_pattern,current_page, selenium_options):
        current_page += 1
        page = self.search_kw(keyword_pattern,current_page, selenium_options)
        return page, current_page

    # Changing block ends here

    def extract_links_content(self, links, selenium_options):
        links_content = []
        driver = webdriver.Firefox(selenium_options)
        for url in links:
            driver.get(url)
            html_content = driver.page_source
            links_content.append(html_content)
        return links_content

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