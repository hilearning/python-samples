# 从列表中删除重复项
def remove_duplicates(items):
    return list(set(items))

items = [1, 2, 2, 3, 4, 4, 5]
unique_items = remove_duplicates(items)
print(f"List without duplicates: {unique_items}")
