# 命令行计算器
def calculator():
    expression = input("Enter an expression (e.g., 2 + 3): ")
    try:
        result = eval(expression)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")

calculator()
