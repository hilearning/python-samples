# 在文件中搜索特定内容
def search_in_file(file_path, keyword):
    with open(file_path, 'r') as file:
        for line_num, line in enumerate(file, 1):
            if keyword in line:
                print(f"Found '{keyword}' at line {line_num}: {line.strip()}")

search_in_file('example.txt', 'Python')  # 替换为实际文件路径和关键词
