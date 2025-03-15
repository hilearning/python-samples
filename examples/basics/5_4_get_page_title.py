# 使用BeautifulSoup爬取网页标题
from bs4 import BeautifulSoup
import requests

def get_page_title(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.title.string

title = get_page_title("https://www.example.com")
print("Page title:", title)
