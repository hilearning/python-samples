# 下载网页内容并保存为HTML文件
import requests

def download_webpage(url, save_path):
    response = requests.get(url)
    with open(save_path, 'w', encoding='utf-8') as file:
        file.write(response.text)
    print(f"Webpage saved to {save_path}")

download_webpage("https://www.example.com", "example.html")
