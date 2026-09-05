# 打印所有用户城市
def print_user_city(users):
    print('\n------------打印所有用户城市------------\n')
    for user in users:
        print(f"{user['name']} → {user['address']['city']}")

# 按城市筛选
def filter_city_user(users):
    try:
        print('\n------------按城市筛选------------\n')
        city_input = input('请输入城市：')
        city_users = []
        for user in users:
            if city_input.lower() in user['address']['city'].lower():
                city_users.append(f"{user['name']} → {user['address']['city']}")
        
        if city_users:
            print(f"找到 {len(city_users)} 个用户：")
            print('\n'.join(city_users))
        else:
            print(f"没有找到 {city_input} 的用户")
    except KeyboardInterrupt:
        print('用户主动退出程序')

# 统计每个城市有多少用户
def count_city_users(users):
    print('\n------------统计每个城市有多少用户------------\n')
    city_users_cnt = {}
    for user in users:
        if user['address']['city'] in city_users_cnt:
            city_users_cnt[user['address']['city']] += 1
        else:
            city_users_cnt[user['address']['city']] = 1

    for city, cnt in city_users_cnt.items():
        print(f"{city}: {cnt}")