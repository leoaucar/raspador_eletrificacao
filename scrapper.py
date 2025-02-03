import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import csv


class Website_Scrapper:
    def __init__(self,website,url,id):
        self.website = website
        self.url = url
        self.id = id

    def kw_pattern_maker(self, keyword):
        pattern = keyword.replace(' ', '+')
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
            print("extracting", url)
            driver.get(url)
            html_content = driver.page_source
            links_content.append((html_content,url))
        return links_content

class Content_Cleaner:
    def __init__(self,website, id):
        self.website = website
        self.id = id

    def process_html(self, content):
        soup = BeautifulSoup(content, "html.parser")
        return soup

# This will change in inheritance
    def extract_title(self, soup):
        title = soup.find('h1', class_="post-title single-post-title entry-title")
        return title.text

    def extract_main_text(self, soup):
        main_text = soup.find('div',class_="post-entry blockquote-style-1")
        return main_text.text

    def extract_author(self, soup):
        pass
    def extract_date(self, soup):
        date = soup.find('time',class_="entry-date published")
        return date['datetime']
        
    def extract_images(self, content):
        pass
# Changing block ends here

    def save_csv(self, title,text,author,date, filename,kw,url):

        file_name = filename+"_data.csv"
        print("saving", file_name)

        # Open the file in append mode
        with open(file_name, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            # Write the header only if the file is empty
            if file.tell() == 0:  # Check if the file is empty
                writer.writerow(["Title","Text","Author", "Date"])
            
            # Write the data
            writer.writerow([title,text, author, date, kw, url])

        print(f"Data saved to {file_name}")


    def save_sql(self, title,text,author,date):
        pass