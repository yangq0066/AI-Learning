import json
import requests
from api import get_users, get_user
from utils import print_users, print_user, filter_city_users

while True:
    try:
        print(f"""
    ====== 用户信息查询器 ======

    1. 获取所有用户
    2. 查询指定用户
    3. 查看用户所在城市
    4. 保存用户数据
    5. 退出程序

    """)
        
        num = int(input('请选择：'))
        match num:
            case 1:
                users = get_users()
                print('6666-', users)
                print_users(users)
            case 2:
                user_id = int(input('请输入用户 ID：'))
                user = get_user(user_id)

                if user:
                    print_user(user)
                else:
                    print('❌  用户不存在 ')
            case 3:
                city = input('请输入城市：')
                users = get_users()
                city_users = filter_city_users(users, city)

                if city_users:
                    print(f"\n{city} 包含用户：")
                    print_users(city_users)
                else:
                    print(f"未找到【{city}】城市的用户")
            case 4:
                users = get_users()
                with open('day05/quiz/users.json', 'w', encoding='utf-8') as file:
                    json.dump(users, file, ensure_ascii=False, indent=2)
                print('✔️  users.json 文件保存成功')
            case 5: 
                print('✔️  已选择退出')
                break
            case _:
                print('❌  无法识别操作序号')
    
    except ValueError:
        print('❌  输入值类型有误')

    except requests.RequestException as e:
        print(f"❌  {e}")