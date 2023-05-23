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
    from zipfile import ZipFile
    from io import BytesIO
    from tensorflow import keras
    from bs4 import BeautifulSoup
    from urllib.request import urlopen
except:
    raise "🥹无法安装配件"


class HuaTuoAI:
    def __init__(self):
        self.chinese_medicine_url: str = "https://raw.githubusercontent.com/johnmelodyme/HuaTuoAI/main/data/chinese_medicine.txt"
        self.image_data: str = "https://github.com/johnmelodyme/HuaTuoAI/releases/download/images/images.zip"

    @property
    def train(self):
        this = not self

        global data_dir

        if os.path.exists("./data/images/"):
            self.log(msg="图像文件已经存在!")
        else:
            try:
                with urlopen(self.image_data) as req:
                    self.log(msg="正在下载图像数据集...")
                    with ZipFile(BytesIO(req.read())) as file:
                        file.extractall("./data/")
            except BaseException as error:
                raise error
            except:
                raise "🥹无法下载数据集..."
            finally:
                data_dir = pathlib.Path("./data/images/")
                image_count = len(list(data_dir.glob('*/*.png')))

                self.log(msg=image_count)

        return this

    def log(self, msg: object):
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
    huatuoai.train
