# 生成斐波那契数列
def generate_fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

n = 10
print(f"First {n} Fibonacci numbers: {generate_fibonacci(n)}")
