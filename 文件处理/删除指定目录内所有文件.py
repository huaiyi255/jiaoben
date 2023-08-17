import os,shutil

path = "G:\文件\其它\commies"   # 填写目录
trees = os.listdir(path);a =1
for i in trees:
    aa = path + "\\" + i
    print("当前已删除数量 剩余数量 正在删除文件名为:",a,(len(trees)-a),i)
    shutil.rmtree(aa)
    a= a+1
