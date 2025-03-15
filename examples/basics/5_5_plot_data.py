# 使用matplotlib绘制简单的折线图
import matplotlib.pyplot as plt

def plot_data(x, y):
    plt.plot(x, y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Simple Line Plot')
    plt.show()

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plot_data(x, y)
