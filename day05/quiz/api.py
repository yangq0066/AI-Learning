import requests

# 获取所有用户
def get_users():
   response = requests.get('https://jsonplaceholder.typicode.com/users')
   users = response.json()
   return users

# 查询指定用户
def get_user(id):
   response = requests.get(f"https://jsonplaceholder.typicode.com/users/{id}")
   user = response.json()
   return user