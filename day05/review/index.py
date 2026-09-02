import json

users = [
    {"name": "张三", "age": 25},
    {"name": "李四", "age": 30},
    {"name": "王五", "age": 22}
]

# 返回年龄 ≥ 25 的用户
def get_adult_users(users):
    adult_users = []

    for user in users:
        if user['age'] >= 25:
            adult_users.append(user)

    return adult_users

print(get_adult_users(users))

# 计算所有用户的平均年龄
def calculate_average(users):
    age_sum = 0

    for user in users:
        age_sum += user['age']

    return (round(age_sum / len(users)))

print(calculate_average(users))

# 把结果保存成：result.json，然后再读取出来
with open("day05/review/result.json", 'w+', encoding='utf-8') as file:
    json.dump(users, file, ensure_ascii=False, indent=2)
    file.seek(0)
    print(file.read())