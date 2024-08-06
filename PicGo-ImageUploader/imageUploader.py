import time

import keyboard
import pyperclip
import requests
import json


def send_post_request_and_simulate_paste():
    url = "http://127.0.0.1:36677/upload"
    response = requests.post(url)

    if response.status_code == 200:
        try:
            data = response.json()
            if data.get("success") and data.get("result"):
                image_url = data["result"][0]
                image_name = image_url.split("/")[-1]
                pyperclip.copy(
                    f'![image-{image_name}](https://carvin-note.oss-cn-shenzhen.aliyuncs.com/img/{image_name})')
                simulate_ctrl_v()
            else:
                print("Requests Success, while get the wrong data.")
        except json.JSONDecodeError:
            print("Response Fail! Not a json data.")
    else:
        print(f"Request Fail! Status: {response.status_code}")


def simulate_ctrl_v():
    keyboard.press_and_release('ctrl+v')
    time.sleep(0.5)
    keyboard.press_and_release('end')
    print("Ctrl+V and Click End Key")


def listen_for_shortcut():
    print("Listening for Ctrl+`shortcut key...")
    while True:
        if keyboard.is_pressed('ctrl+`'):
            print("Ctrl+`is detected, processing begins...")
            send_post_request_and_simulate_paste()


if __name__ == "__main__":
    listen_for_shortcut()
