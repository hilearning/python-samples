# 列出目录中的所有文件
import os

def list_files(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

files = list_files('.')  # 当前目录
print("Files in directory:", files)
