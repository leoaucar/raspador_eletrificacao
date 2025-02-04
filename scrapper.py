import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import csv
import html
import re

#base class for scrapping
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
        driver.quit()
        return links_content

#basic class for html processsing and info extractions
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
        timestamp = str(date['datetime'])
        pattern = r"(\d{4})-(\d{2})-(\d{2})T\d{2}:\d{2}:\d{2}[-+]\d{2}:\d{2}"
        formatted_date = re.sub(pattern, r"\3/\2/\1", timestamp)
        return formatted_date
        
    def extract_images(self, content):
        pass
# Changing block ends here

    def save_csv(self, title,text,author,date, filename,kw,url):

        file_name = filename+"_data.csv"

        # Open the file in append mode
        with open(file_name, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            # Write the header only if the file is empty
            if file.tell() == 0:  # Check if the file is empty
                writer.writerow(["Titulo","Texto Noticia","Autor", "Data", "Buscas", "URL"])
            
            # Write the data
            writer.writerow([title,text, author, date, kw, url])

        print(f"Data saved to {file_name}")


    def save_sql(self, title,text,author,date):
        pass


##CLASSES PARA O AUTODATA
class AutoDataScrapper(Website_Scrapper):
    def search_kw(self, keyword_pattern, current_page, selenium_options):
        driver = webdriver.Firefox(selenium_options)
        schema_url = "https://"
        final_url = schema_url+self.url+'/busca/?p='+ str(current_page) +'&palavra='+keyword_pattern
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
        for link in soup.find_all('li', class_="titulo-ultimas-noticias"):
            new_links.append(link.find('a').get('href'))
        return new_links

class AutoDataCleaner(Content_Cleaner):
    # This will change in inheritance
    def extract_title(self, soup):
        title = soup.find('h1', class_="titulo-post-noticia-interna")
        return title.text

    def extract_main_text(self, soup):
        main_text = str(soup.find('iframe'))
        main_text = html.unescape(main_text)
        # Remove todas as tags HTML
        main_text = re.sub(r'<[^>]+>', '', main_text)
        main_text.strip()
        lines = main_text.strip().split("\n")
        cleaned_lines = lines[1:-1]
        cleaned_text = re.sub(r'\n\s*\n+', '\n\n', "\n".join(cleaned_lines))
        return cleaned_text

    def extract_author(self, soup):
        pass
    def extract_date(self, soup):
        date = soup.find('div',class_="data-noticia")
        return date.text
        
    def extract_images(self, content):
        pass

#CLASSES PARA DIARIO ABC
class DiarioABCScrapper(Website_Scrapper):
    def kw_pattern_maker(self, keyword):
        pattern = keyword.replace(' ', '%20')
        return pattern

    def search_kw(self, keyword_pattern, current_page, selenium_options):
        driver = webdriver.Firefox(selenium_options)
        schema_url = "https://"
        final_url = schema_url+self.url+'/Buscas/Home?palavra='+keyword_pattern+ '&pagina='+ str(current_page)
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
        for link in soup.find_all('a', class_="titulo"):
            new_links.append("https://www.dgabc.com.br"+link.get('href'))
        return new_links

class DiarioABCCleaner(Content_Cleaner):
    # This will change in inheritance
    def extract_title(self, soup):
        title = soup.find('div', class_="_noticiaTitulo")
        title = title.text.strip()
        return title

    def extract_main_text(self, soup):
        main_text = soup.find('div', class_="_noticiaMateria")
        lines = main_text.text.strip().split("\n")
        lines = lines[:-2]
        cleaned_text = re.sub(r'\n\s*\n+', '\n\n', "\n".join(lines))
        return cleaned_text

    def extract_author(self, soup):
        pass

    def extract_date(self, soup):
        date = soup.find('div',class_="_noticiaDataPublicacao")
        date = date.text.strip()[0:9]
        return date
        
    def extract_images(self, content):
        pass

##FUTURAS CLASSES PARA MAIS SITES
