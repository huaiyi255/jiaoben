import os  
import hashlib  
  
def calculate_file_hash(file_path):  
    """计算文件的哈希值"""  
    hash_func = hashlib.sha256()  
    with open(file_path, 'rb') as file:  
        for chunk in iter(lambda: file.read(4096), b""):  
            hash_func.update(chunk)  
    return hash_func.hexdigest()  
  
def find_duplicate_files(directory):  
    """在指定目录中查找重复文件"""  
    file_size_dict = {}  
    for root, _, files in os.walk(directory):  
        for file in files:  
            file_path = os.path.join(root, file)  
            file_size = os.path.getsize(file_path)  
            if file_size in file_size_dict:  
                file_size_dict[file_size].append(file_path)  
            else:  
                file_size_dict[file_size] = [file_path]  
  
    duplicate_files = [files for files in file_size_dict.values() if len(files) > 1]  
    return duplicate_files  
  
def main(path):  
    directory = path  
  
    if not os.path.exists(directory):  
        print("目录不存在")  
        return  
  
    duplicate_files = find_duplicate_files(directory)  
  
    if duplicate_files:  
        print("找到重复文件:")  
        for files in duplicate_files:  
            file_hash_dict = {}  
            for file_path in files:  
                file_hash = calculate_file_hash(file_path)  
                if file_hash in file_hash_dict:  
                    print("相同文件:")  
                    print(file_hash_dict[file_hash])  
                    print(file_path)  
                else:  
                    file_hash_dict[file_hash] = file_path  
    else:  
        print("未找到重复文件")  
  
if __name__ == "__main__":  
    path = "E:\\files\\"  
    main(path)
