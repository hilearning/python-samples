# 下载图片并保存到本地
import requests

def download_image(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as file:
        file.write(response.content)

image_url = "https://www.example.com/image.jpg"
download_image(image_url, "image.jpg")
print("Image downloaded successfully!")
