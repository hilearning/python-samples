# 将文件压缩为ZIP格式
import zipfile

def zip_files(file_paths, output_zip):
    with zipfile.ZipFile(output_zip, 'w') as zipf:
        for file in file_paths:
            zipf.write(file)

files_to_zip = ['file1.txt', 'file2.txt']  # 替换为实际文件路径
zip_files(files_to_zip, 'archive.zip')
print("Files zipped successfully!")
