# 读文件
# 写法一
file = open("day04/message.txt", 'r', encoding='utf-8')
content = file.read()
print(content)
file.close()

print('----------------------------------------------------')

# 写法二
with open("day04/message.txt", 'r', encoding="utf-8") as file:
    content = file.read()

print(content)

print('----------------------------------------------------')

# 写文件
with open("day04/output.txt", 'w+', encoding="utf-8") as file:
    file.write('这是一个使用 file.write 写入的新文件') # 写完后文件指针在末尾
    file.seek(0) # 文件指针回到开头
    print(file.read())

print('----------------------------------------------------')

with open("day04/message.txt", 'a+', encoding="utf-8") as file:
    file.write('\n\n这是使用 mode = a 写入的内容')
    file.seek(0)
    print(file.read())

print('----------------------------------------------------')

import json

with open('day04/devices.json', 'r', encoding='utf-8') as file:
   devices = json.load(file)
   print(devices)

devices[1]['online'] = True

with open('day04/devices.json', 'w+', encoding='utf-8') as file:
    json.dump(devices, file, ensure_ascii=False, indent=2)
    file.seek(0)
    print(file.read())

print('----------------------------------------------------')

try:
    number = int(input("请输入："))
    print(number)
except ValueError:
    print('请输入整数！')