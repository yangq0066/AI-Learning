def print_users(users):
    for i, user in enumerate(users):
        print(f"{i + 1}. {user['name']}")

def print_user(user):
    print(f"""
用户信息
----------------
姓名：{user['name']}
用户名：{user['username']}
邮箱：{user['email']}
城市：{user['address']['city']}
公司：{user['company']['name']}
    """)

def filter_city_users(all_users, city):
    city_users = []

    for user in all_users:
        if user['address']['city'].lower() == city.lower():
            city_users.append(user)
    
    return city_users