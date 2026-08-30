def get_online_devices(devices):
    online_devices = []

    for device in devices:
        if device['online']:
            online_devices.append(device)

    return online_devices


def get_offline_devices(devices):
    offline_devices = []

    for device in devices:
        if not device['online']:
            offline_devices.append(device)

    return offline_devices


def print_devices(devices):
    for device in devices:
        status = '在线' if device['online'] else '离线'
        print(f"{device['name']} - {status}")