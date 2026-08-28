devices = [
    {
        'id': 1,
        'name': '设备001',
        'online': True
    },
    {
        'id': 2,
        'name': '设备002',
        'online': False
    },
    {
        'id': 3,
        'name': '设备003',
        'online': False
    },
    {
        'id': 4,
        'name': '设备004',
        'online': True
    }
]

for device in devices:
    if device['online'] == False: # 写法一
        print(f'离线设备：{device['name']}');

for device in devices:
    if not device['online']: # 写法二
        print(f'离线设备：{device['name']}');

print('----------------------------------------------------')

print(f'设备总数：{len(devices)}')

onlineCount = 0
offlineCount = 0

for device in devices:
    if device['online'] == True:
       onlineCount = onlineCount + 1;
    elif device['online'] == False:
        offlineCount = offlineCount + 1;

print(f'在线设备数：{onlineCount}')
print(f'离线设备数：{offlineCount}')

print('----------------------------------------------------')

devices2 = [
    {
        "id": 1,
        "name": "教室终端001",
        "ip": "192.168.1.101",
        "online": True
    },
    {
        "id": 2,
        "name": "教室终端002",
        "ip": "192.168.1.102",
        "online": False
    },
    {
        "id": 3,
        "name": "教室终端003",
        "ip": "192.168.1.103",
        "online": True
    },
    {
        "id": 4,
        "name": "教室终端004",
        "ip": "192.168.1.104",
        "online": False
    }
]

print('所有设备名称：')
for device in devices2:
    print(device['name']);

print('----------------------------------------------------')

print('所有设备IP：')
for device in devices2:
    print(device['ip']);

print('----------------------------------------------------')

print('所有在线设备:')
for device in devices2:
    if device['online']:
        print(f'{device['name']} - {device["ip"]}');

print('----------------------------------------------------')

print('所有离线设备:')
for device in devices2:
    if not device['online']:
        print(f'{device['name']} 当前离线，IP：{device["ip"]}')