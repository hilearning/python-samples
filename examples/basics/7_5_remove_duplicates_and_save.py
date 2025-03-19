# 从列表中去除重复项并保存到文件
def remove_duplicates_and_save(data, output_file):
    unique_data = list(set(data))
    with open(output_file, 'w') as file:
        for item in unique_data:
            file.write(f"{item}\n")
    print(f"Unique data saved to {output_file}")

data = ["apple", "banana", "apple", "orange", "banana"]
remove_duplicates_and_save(data, 'unique_items.txt')
