# 过滤列表中的数据
def filter_data(data, condition):
    return [item for item in data if condition(item)]

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_data = filter_data(data, lambda x: x % 2 == 0)  # 过滤偶数
print("Filtered data:", filtered_data)
