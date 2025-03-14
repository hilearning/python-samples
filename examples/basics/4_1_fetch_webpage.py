# 使用requests库获取网页内容
import requests

def fetch_webpage(url):
    response = requests.get(url)
    return response.text

url = "https://www.example.com"
webpage_content = fetch_webpage(url)
print(webpage_content[:200])  # 打印前200个字符
