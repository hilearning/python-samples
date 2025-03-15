# 对列表中的数据进行排序
def sort_data(data):
    return sorted(data, key=lambda x: x['age'])

data = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 20}, {'name': 'Charlie', 'age': 30}]
sorted_data = sort_data(data)
print("Sorted data:", sorted_data)
