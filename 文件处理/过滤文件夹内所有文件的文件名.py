import os

path = 'E:\\111\\'
filelists = os.listdir(path)
n = 1
# 替换改名
for filelist in filelists:
    if ('《' in filelist) or ('》' in filelist):
        name = filelist.replace('《','').replace('》','')
        oldname = path + filelist
        newname = path + name
        os.rename(oldname, newname)
print("已完成！")
