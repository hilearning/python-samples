# 解析JSON数据
import json

json_data = '{"name": "Alice", "age": 25, "city": "New York"}'
data = json.loads(json_data)
print(f"Name: {data['name']}, Age: {data['age']}, City: {data['city']}")
