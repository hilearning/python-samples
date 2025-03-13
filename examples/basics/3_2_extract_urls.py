# 从文本中提取URL
import re

def extract_urls(text):
    return re.findall(r'https?://\S+', text)

text = "Visit https://www.example.com or http://www.test.com for more info."
urls = extract_urls(text)
print("Found URLs:", urls)
