from tuyapy import TuyaApi
import time


def lamp_operations(decision: str):
    USERNAME = ""
    PASSWORD = ""
    COUNTRY_CODE = "poland"
    api = TuyaApi()
    api.init(USERNAME, PASSWORD, COUNTRY_CODE)

    lampka_nocna = {'bf5a8b5a2c599f05a4i2nd': "Night lamp"}
    known_devices_list = [lampka_nocna]

    print("list of available devices: ")
    for device in api.get_all_devices():
        # id = device.object_id()

        for known_device in known_devices_list:
            key, value = list(known_device.items())[0]
            if device.object_id() == key:
                print(value)

    if decision == "off":
        api.get_device_by_id("bf5a8b5a2c599f05a4i2nd").turn_off()
    elif decision == "on ":
        api.get_device_by_id("bf5a8b5a2c599f05a4i2nd").turn_on()
    print("     ---------------------------------------------------  ")
    print("   /                                                   /")
    print(f"  /   Device - {value}  - current status - {decision}     /")
    print(" /                                                   /")
    print(" ---------------------------------------------------")
    time.sleep(2)

