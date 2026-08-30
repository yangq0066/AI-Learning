import json
from helper_functions import get_online_devices, get_offline_devices, print_devices

try:
    with open('day04/devices.json', 'r', encoding='utf-8') as file:
       devices = json.load(file)

    online_devices = get_online_devices(devices)

    offline_devices = get_offline_devices(devices)

    print('====== 设备列表 ======\n')
    print_devices(devices)

    print('\n====== 统计 ======\n')
    print(f"在线设备：{len(online_devices)}")
    print(f"离线设备：{len(offline_devices)}")

except FileNotFoundError:
    print('没有找到 devices.json 文件')

except json.JSONDecodeError:
    print('JSON 格式有误')