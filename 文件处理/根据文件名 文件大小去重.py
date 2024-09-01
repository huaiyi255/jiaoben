geimport os

def find_and_delete_duplicates(folder1, folder2):
    # 获取两个文件夹中的所有文件名
    files1 = set(os.listdir(folder1))
    files2 = set(os.listdir(folder2))

    # 找到两个文件夹中共有的文件名
    common_files = files1.intersection(files2)

    for file in common_files:
        path1 = os.path.join(folder1, file)
        path2 = os.path.join(folder2, file)

        # 检查文件是否存在
        if os.path.exists(path1) and os.path.exists(path2):
            size1 = os.path.getsize(path1)
            size2 = os.path.getsize(path2)

            # 删除较小的文件
            if size1 < size2:
                os.remove(path1)
                print(f"Deleted {path1} because it is smaller than {path2}")
            elif size2 < size1:
                os.remove(path2)
                print(f"Deleted {path2} because it is smaller than {path1}")
            else:
                print(f"Files {path1} and {path2} are of equal size and will not be deleted.")

if __name__ == "__main__":
    folder1 = "C:\\"
    folder2 = "E:\\"
    find_and_delete_duplicates(folder1, folder2)

# 判断两文件夹内是否存在文件名相同的文件，如果存在就判断大小，删除较小的文件
