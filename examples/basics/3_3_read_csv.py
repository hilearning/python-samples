# 读取CSV文件并打印内容
import csv

def read_csv(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

read_csv('data.csv')  # 替换为你的CSV文件路径
