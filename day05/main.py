import requests
import json

def get_users():
   response = requests.get('https://jsonplaceholder.typicode.com/users')
   return response.json()

users = get_users()
for user in users:
   print(user['name'])

#######################################
 
def get_user_names(users):
   user_names = []

   for user in users:
      user_names.append(user['name'])
   
   return user_names

user_names = get_user_names(users)
print(user_names)

#######################################
try:
  response = requests.get(
     'https://jsonplaceholder.typicode.com/users1',
      timeout=5
   )
  
  response.raise_for_status()

  users = response.json()

except requests.RequestException as e:
   print('请求失败：', e)

#######################################
   
response = requests.get('https://jsonplaceholder.typicode.com/users')
users = response.json()

with open('day05/users.json', 'w', encoding='utf-8') as file:
   json.dump(users, file, ensure_ascii=False, indent=2)
