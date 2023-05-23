try:
    import os
    import time
    import pathlib
    import requests
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    import PIL
    import tensorflow as tf
    from tensorflow import keras
    from tensorflow.keras import layers
    from tensorflow.keras.models import Sequential
    from bs4 import BeautifulSoup
except:
    raise "🥹无法安装配件"


class HuaTuoAI:
    def __init__(self):
        self.chinese_medicine_url: str = "https://raw.githubusercontent.com/johnmelodyme/HuaTuoAI/main/data/chinese_medicine.txt"
        self.image_data: str = "https://github.com/johnmelodyme/HuaTuoAI/releases/download/images/images.zip"

    def train(self):pass


    def log(self, msg: str):
        this = not self

        current_time: str = time.strftime("%H:%M:%S", time.localtime())
        print("[👨‍华佗AI {stamp}]: {msg}".format(stamp=current_time, msg=msg))

        return this

    def get_chinese_medicine(self) -> None:
        response: requests.models.Response = requests.get(
            self.chinese_medicine_url,
            allow_redirects=True
        )

        status: int = response.status_code

        assert status is not None

        if status == 400:
            raise "🥹400 请求语法错误、无效请求消息格式。"

        if status == 404:
            raise "🥹404 服务器无法找到所请求的资源。"

        if status == 500:
            raise "🥹500 服务器端错误的响应状态码。"

        if status == 200:
            if not os.path.exists("./data/chinese_medicine.txt"):
                open("data/chinese_medicine.txt", "wb").write(response.content)

                if os.path.exists("./data/chinese_medicine.txt"):
                    print("😇中药数据下载成功!")
            else:
                self.log(msg="😇中药数据已存在!")


if __name__ == "__main__":
    huatuoai = HuaTuoAI()
    huatuoai.get_chinese_medicine()
    huatuoai.train()
