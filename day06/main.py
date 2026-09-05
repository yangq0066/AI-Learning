# 今日学习：dict / list 强化

import requests
from utils import print_user_city, filter_city_user, count_city_users

try:
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    users = response.json()
except requests.RequestException as e:
    print('请求出错了——', e)

while True:
    print(f"""
====== 用户查询系统 ======
      
1. 查看所有用户城市
2. 按城市查询用户
3. 统计城市用户数
4. 退出 
          
""")
    
    try:
        oper_num = int(input('请选择：'))
        match oper_num:
            case 1:
                print_user_city(users)

            case 2:
                filter_city_user(users)

            case 3:
                count_city_users(users)

            case 4:
                break

            case _:
                print('无法识别的操作')
    except ValueError:
        print('用户输入错误')