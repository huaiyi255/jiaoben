# 将某文件夹内文件名相似项筛选(优化版)(也可以修改一下通过修改时间,文件大小等等来筛选)
# 优化思路，尝试将列表转为字典（字典 和 集合 比 列表 快），结构优化（原始代码，随着listcf的变大，循环的次数会几何倍数的提高，时间也会不断的提升）（for循环的多次嵌套导致时间变多）
import os,difflib,time,re

start1 = time.time()
ccc = 0
listlfag = {'flag':{'this is flag'}}

path = 'E:\\down\\mh\\commies'
path_names = set(os.listdir(path))  # 转换为集合，优化
listlfag1 = []
for aaa in listlfag.keys():
    d = aaa.replace(' ','')
    listlfag1.append(d)   
for n in path_names:
    start = time.time()
    m = n.replace(' ','')  # comic格式化后的命令
    mnum = [int(i) for i in re.findall(r'\d', m)]  # comic名中的数字
    for aa in listlfag.copy().keys():
        d = aa.replace(' ','')
        dnum = [int(i) for i in re.findall(r'\d', d)]  
        similarity = difflib.SequenceMatcher(None, m, d).ratio()
        if (similarity) >= 0.85 and (m not in listlfag1) and (mnum == dnum):
            listlfag[aa].add(n)
        elif m not in listlfag1:
            listlfag.update({m:{m}}) 
    ccc = ccc +1
    end = time.time()
    running_time = end - start
    path_namesnum = ccc/len(path_names)*100
    print(f'num:{ccc},time:{running_time},%:{path_namesnum}%')# print(f'{ccc} {n}')
listcf = []
for aaa in listlfag.copy().values():
    if len(aaa) >= 2:
       listcf.append(aaa)
print(listcf)     # 输出重复项
start2 = time.time()
print('总运行时间为:',start2-start1)

# 原始版本,运行到700多项每一次循环时间会越来越长
'''
将文件夹内所有相似项筛选出来(for循环版,运行到后面运行会越来越慢,直到卡死,当前已筛选3k的文件 后面直接卡死,1k以下文件为最佳)
import os,difflib,time

listlfag = [['this is flag']]
listcf = []
path = 'E:\\down\\mh\\commies'
path_names = os.listdir(path)

# 思路,设定一个列表,里面每一个元素都是列表,如果与里面的元素相似度大于多少就将这个字符串加入到相似度高的列表
ccc = 0
for n in path_names:
    m = n.replace(' ','')
    mnum = [int(i) for i in m if i.isdigit()]
    for a in listlfag:
        num =listlfag.index(a)  # 确定二维列表 第一维的索引
        for b in a:
            d = b.replace(' ','')
            dnum = [int(z) for z in d if z.isdigit()]
            similarity = difflib.SequenceMatcher(None, m, d).ratio()
            if similarity >= 0.85:
                if (n not in b) and (mnum != dnum):
                    listlfag[num].append(n)   
            else:
                if [n] not in listlfag:
                    listlfag.append([n])     
    ccc = ccc +1
    # time.sleep(5)
    print(ccc,len(path_names),ccc/len(path_names))# print(f'{ccc} {n}')
for aaa in listlfag:
    if len(aaa) >= 2:
       listcf.append(aaa)
print(listcf)     # 输出重复项
'''
