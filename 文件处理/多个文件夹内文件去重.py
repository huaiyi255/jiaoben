import os
import hashlib
import argparse

# 定义哈希函数
def calculate_hash(file_path):
    hash_func = hashlib.sha256()
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hash_func.update(chunk)
    return hash_func.hexdigest()

# 解析命令行参数
parser = argparse.ArgumentParser(description='Compare files in multiple folders.')
parser.add_argument('folders', metavar='FOLDER', type=str, nargs='+',
                    help='path to the folder')
args = parser.parse_args()

# 创建一个字典来存储文件的路径及大小
files_dict = {}

# 遍历每个文件夹
for folder in args.folders:
    # 遍历文件夹中的每个文件
    for file_path in os.listdir(folder):
        file_path = os.path.join(folder, file_path)
        # 获取文件大小
        size = os.path.getsize(file_path)
        # 如果文件大小已经存在，就直接来计算hash
        if size in files_dict:
            hash_value1 = calculate_hash(file_path)
            hash_value2 = calculate_hash(files_dict[size])
            if hash_value1 == hash_value2:
                # print(f"文件重复: {file_path} and {files_dict[size]}")
                if len(files_dict[size]) > len(file_path):
                    print(f'删除重复文件: {file_path}')
                    os.remove(file_path)
                else:
                    print(f'删除重复文件: {files_dict[size]}')
                    os.remove(files_dict[size])
        # 将文件的大小和哈希值添加到字典中
        files_dict[size] = file_path

'''
先聚合所有文件信息，文件大小相同就计算hash，hash相等就计算文件名，删除文件名较短的文件

使用：python3 test.py /Users/z/Desktop/1 /Users/z/Desktop/2 /Users/z/Desktop/3
'''

