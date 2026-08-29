devices = [
    {"name": "设备001", "online": True},
    {"name": "设备002", "online": False},
    {"name": "设备003", "online": True},
    {"name": "设备004", "online": False},
]

def get_devices_status(devices):
    lines = []
    for device in devices:
        status = '在线' if device['online'] else '离线'
        lines.append(f"{device['name']} - {status}")
    
    return "\n".join(lines)

def count_online_devices(devices):
    online_count = 0
    for device in devices:
        if device['online']:
            online_count += 1
    
    return online_count

def count_offline_devices(devices):
    offline_count = 0
    for device in devices:
        if not device['online']:
            offline_count += 1
        
    return offline_count

print(f"""====== 设备状态 ======

{get_devices_status(devices)}

====== 统计 ======

在线设备：{count_online_devices(devices)}
离线设备：{count_offline_devices(devices)}
""")