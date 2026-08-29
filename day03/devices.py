devices = [
    {"name": "设备001", "online": True},
    {"name": "设备002", "online": False},
    {"name": "设备003", "online": True},
    {"name": "设备004", "online": False},
]

def get_online_devices(devices):
    online_devices = []

    for device in devices:
        if(device['online']):
            online_devices.append(device);

    return online_devices;

online_devices = get_online_devices(devices)
print(f'所有在线设备：{online_devices}')

print('----------------------------------------------------')

def count_online_devices(devices):
    online_devices_count = 0

    for device in devices:
        if(device['online']):
            online_devices_count = online_devices_count + 1;

    return online_devices_count;

print(f'在线设备总数：{count_online_devices(devices)}')

print('----------------------------------------------------')

def print_devices(devices):
    for device in devices:
        print(f"{device['name']} - {'在线' if device['online'] else '离线'}")

print_devices(devices)