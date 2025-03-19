# 命令行待办事项列表
def todo_list():
    tasks = []
    while True:
        task = input("Add a task (or type 'done' to finish): ")
        if task == 'done':
            break
        tasks.append(task)
    print("Your tasks:", tasks)

todo_list()
