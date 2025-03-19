# 文件重命名工具
import os

def rename_files(directory, prefix):
    for count, filename in enumerate(os.listdir(directory)):
        new_name = f"{prefix}_{count}{os.path.splitext(filename)[1]}"
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
    print("Files renamed successfully!")

rename_files('photos', 'image')  # 替换为实际目录路径和前缀
