# 计算列表中数字的平均值
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print(f"The average is: {average}")
