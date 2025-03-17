# 文件批量重命名
import os

def batch_rename(directory, prefix):
    for count, filename in enumerate(os.listdir(directory)):
        dst = f"{prefix}_{str(count)}.txt"
        src = os.path.join(directory, filename)
        dst = os.path.join(directory, dst)
        os.rename(src, dst)

batch_rename("path/to/directory", "new_name")
