filename = 'E:\\密码字典\\renkoutop.txt'  # 爆破字典
f = open(filename, "r", encoding='UTF-16')  # 设置文件对象
bf_dict = []
lines = f.readlines()  # 将txt文件的所有内容读入到字符串strtxt中
for line in lines:
    bf_dict.append(line.lstrip('查询成功:').rstrip())  # 去除前面的空格或后面的空格或者指定字符串
# bf_dict = strtxt
f.close()  # 将文件关闭
print(bf_dict)
