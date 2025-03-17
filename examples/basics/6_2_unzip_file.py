# 解压缩ZIP文件
import zipfile

def unzip_file(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zipf:
        zipf.extractall(extract_to)
    print(f"Files extracted to {extract_to}")

unzip_file('archive.zip', 'extracted_files')  # 替换为实际ZIP文件路径和目标目录
