# picacg pc 漫画格式转换为komga可以识别的，或者压缩进行保存，需要在picacg漫画所在根目录运行
# picacg pc github：https://github.com/tonquer/picacg-qt
# komga github：https://github.com/gotson/komga
import os,sys,zipfile,natsort

def comic_list():
    # 获取到当前文件夹内所有漫画名
    path = os.path.dirname(__file__)
    path_names = os.listdir()
    path_names.remove(os.path.basename(sys.argv[0]))
    # 获取漫画的所有漫画名路径与对应章节名 形成一对对键值对 保存在一个字典内
    path_all = {}
    for i in path_names:
        path111 = path + '\\' +i + '\\original\\'
        dirlist = os.listdir(str(path111))  # natsort.natsorted()
        dirlist2 = []
        for a in dirlist:
            b = path + '\\' +i + '\\original\\' + a + '\\'
            dirlist2.append([a,b])
        path_all.update({i:natsort.natsorted(dirlist2)}) 
    return path_all

# 传入文件名列表,对应要压缩的文件夹
def zippath(path_all,filepath):
    print('初始化存放文件目录:',filepath)
    try:
        os.mkdir(filepath)
    except FileExistsError:
        print('当前初始化目录已存在')
    comic_path_names = list(path_all.keys())  # 获取所有comic名
    for i in comic_path_names:
        path1 = filepath + '\\' + i
        try:
            os.mkdir(path1)
        except FileExistsError:
            pass
        for a in path_all[i]: # 获取其值   a = ['第1-7話', 'E:\\test\\555\\original\\第1-7話\\']
            filea = os.listdir(a[1])  # 获取当前章节内的所有文件名
            zippath = path1 + '\\' + a[0] + '.zip'
            if os.path.exists(zippath) == True:
                os.remove(zippath)
            with zipfile.ZipFile(zippath, 'a', compression=zipfile.ZIP_DEFLATED) as out_file:
                for bbb in filea:
                    ddd = a[1] + bbb
                    out_file.write(ddd,bbb)
        print(i,'已完成',)

def start():
    filepath = 'e:\\comic'
    path_all = comic_list()
    zippath(path_all,filepath)

start()
