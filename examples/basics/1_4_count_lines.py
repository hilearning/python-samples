# 简单的文件读取与统计行数
def count_lines(filename):
    with open(filename, 'r') as file:
        return len(file.readlines())

filename = 'example.txt'
line_count = count_lines(filename)
print(f"The file '{filename}' has {line_count} lines.")
