# 简单的温度转换器（摄氏转华氏）
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = 25
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is {fahrenheit}°F")
