# -*- coding: UTF-8 -*-
try:
    import os
    import tensorflow as tf
    import numpy as np
    import matplotlib
    import matplotlib.pyplot as 图表
    from typing import Tuple
    from datetime import datetime
    import PIL
    import scipy
    import tensorflow as tf
    from zipfile import ZipFile
    from io import BytesIO
    from PIL import Image
    from bs4 import BeautifulSoup
    from urllib.request import urlopen
    from colors import pink_back, purple_back, green_back
    from keras.preprocessing.image import ImageDataGenerator
    from keras.models import Sequential
    from keras.layers import Conv2D, MaxPooling2D
    from keras.layers import Activation, Dropout, Flatten, Dense
    from keras import backend as _keras
except ImportError:
    raise ImportError("🥹无法安装配件")
finally:
    pass


class 华佗AI:
    def __init__(self, 展示: bool) -> None:
        super(华佗AI, self).__init__()

        matplotlib.rcParams["font.family"] = "Heiti TC"

        assert tf.__version__.startswith("2")

        self.chinese_medicine_url: str = (
            "https://raw.githubusercontent.com/johnmelodyme/HuaTuoAI/main/data/chinese_medicine.txt"
        )
        self.image_data: str = (
            "https://github.com/johnmelodyme/HuaTuoAI/releases/download/images/images.zip"
        )
        self.image_width: int = 224
        self.image_height: int = 224
        self.train_sample: int = 300
        self.validation_sample: int = 100
        self.epochs: int = 7
        self.batch_size: int = 16
        self.format: str = "channels_first"
        self.model: Sequential = Sequential()
        self.activation: list = ["relu", "sigmoid"]
        self.loss_func: str = "binary_crossentropy"
        self.class_mode: str = "binary"
        self.optimiser: str = "rmsprop"
        self.metrics: list = ["accuracy"]
        self.binary_extension: str = ".h5"
        self.名称: str = "华佗AI"
        self.展示: bool = 展示
        self.图片文件 = "./data/images/"
        self.seed: int = 21
        self.图像高度: int = 60
        self.图像宽度: int = 60
        self.批量的大小: int = 50
        self.轴: str | None = "off"
        self.活化: str | None = "relu"
        self.中药材料: list | any = ["丁公藤", "金银花", "罗汉果", "人参片", "绿豆"]
        self.优化器: str | None = "adam"
        self.纪元: int = 5

    def 训练数据(self) -> None:
        self.记录(信息="TensorFlow 版本 |> {}".format(tf.__version__))

        try:
            if os.path.exists(self.图片文件):
                训练目录: tensorflow.python.data.ops.batch_op._BatchDataset = (
                    tf.keras.utils.image_dataset_from_directory(
                        self.图片文件,
                        image_size=(self.图像高度, self.图像宽度),
                        batch_size=self.批量的大小,
                    )
                )

                估价目录: tensorflow.python.data.ops.batch_op._BatchDataset = (
                    tf.keras.utils.image_dataset_from_directory(
                        self.图片文件,
                        image_size=(self.图像高度, self.图像宽度),
                        batch_size=self.批量的大小,
                    )
                )

                测试目录: tensorflow.python.data.ops.batch_op._BatchDataset = (
                    tf.keras.utils.image_dataset_from_directory(
                        self.图片文件,
                        image_size=(self.图像高度, self.图像宽度),
                        batch_size=self.批量的大小,
                    )
                )

                if self.展示:
                    图表.figure(figsize=(6, 6))
                    图表.suptitle(self.名称)

                for 照片, 名称 in 训练目录.take(1):
                    for 药 in range(9):
                        图表.subplot(3, 3, (药 + 1))
                        图表.imshow(照片[药].numpy().astype("uint8"))
                        图表.title(
                            label=self.中药材料[名称[药]], fontsize=15, color="green"
                        )
                        图表.axis(self.轴)

                if self.展示:
                    图表.show()

                训练模型 = tf.keras.Sequential(
                    [
                        tf.keras.layers.Rescaling(1.0 / 255),
                        tf.keras.layers.Conv2D(32, 1, activation=self.活化),
                        tf.keras.layers.MaxPool2D(),
                        tf.keras.layers.Conv2D(32, 1, activation=self.活化),
                        tf.keras.layers.MaxPool2D(),
                        tf.keras.layers.Conv2D(32, 1, activation=self.活化),
                        tf.keras.layers.MaxPool2D(),
                        tf.keras.layers.Flatten(),
                        tf.keras.layers.Dense(128, activation=self.活化),
                    ]
                )

                训练模型.compile(
                    optimizer="adam",
                    loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
                    metrics=["accuracy"],
                )

                训练模型.fit(训练目录, validation_data=训练目录, epochs=self.纪元)

            else:
                self.记录(信息=f"{self.图片文件} 不存在")
        except Exception as e:
            raise e
        finally:
            pass

    def 记录(self, 信息: str) -> None:
        现在: object = datetime.now()
        目前时间: object = 现在.strftime("%H:%M:%S")

        print(green_back + f"华佗AI[{目前时间}] {str(信息)}")

    def train(self) -> None:
        global input_shape

        if os.path.exists("./data/images/"):
            self.log(msg="😇图像文件已经存在!")
        else:
            try:
                with urlopen(self.image_data) as req:
                    self.log(msg="😇正在下载图像数据集...")
                    with ZipFile(BytesIO(req.read())) as file:
                        file.extractall("./data/")
            except BaseException as error:
                raise error
            except:
                raise "🥹无法下载数据集..."

        data_dir = pathlib.Path("./data/images/")
        input_dir = pathlib.Path("./data/input/")
        image_count = len(list(data_dir.glob("*/*.png")))
        _image_count = len(list(input_dir.glob("*/*.png")))

        self.log(msg="😇Data 的数据集文件夹包含{}个图像!".format(image_count))
        self.log(msg="😇Input 的数据集文件夹包含{}个图像!".format(_image_count))

        if _keras.image_data_format() == self.format:
            input_shape = (3, self.image_width, self.image_height)
        else:
            input_shape = (self.image_width, self.image_height, 3)

        self.model.add(Conv2D(32, (2, 2), input_shape=input_shape))
        self.model.add(Activation(self.activation[0]))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))

        self.model.add(Conv2D(32, (2, 2)))
        self.model.add(Activation(self.activation[0]))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))

        self.model.add(Conv2D(64, (2, 2)))
        self.model.add(Activation(self.activation[0]))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))

        self.model.add(Flatten())
        self.model.add(Dense(64))
        self.model.add(Activation(self.activation[0]))

        self.model.add(Dropout(0.5))
        self.model.add(Dense(1))
        self.model.add(Activation(self.activation[1]))

        # 通过指定损失函数、优化器和评估度量，准备在数据集上训练的模型。
        self.model.compile(
            loss=self.loss_func, optimizer=self.optimiser, metrics=self.metrics
        )

        tn_datagen: ImageDataGenerator = ImageDataGenerator(
            rescale=1.0 / 255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True
        )

        test_datagenerator: ImageDataGenerator = ImageDataGenerator(rescale=1.0 / 255)

        train_generator = tn_datagen.flow_from_directory(
            data_dir,
            target_size=(self.image_width, self.image_height),
            batch_size=self.batch_size,
            class_mode=self.class_mode,
        )

        input_generator = test_datagenerator.flow_from_directory(
            input_dir,
            target_size=(self.image_width, self.image_height),
            batch_size=self.batch_size,
            class_mode=self.class_mode,
        )

        self.model.fit_generator(
            train_generator,
            steps_per_epoch=self.train_sample / self.batch_size,
            epochs=self.epochs,
            validation_data=input_generator,
            validation_steps=self.validation_sample // self.batch_size,
        )

        try:

            self.model.save_weights("chinese_medicine{}".format(self.binary_extension))
            self.log(msg="😇训练模型保存为《chinese_medicine.h5》")
            self.convert_to_tflite()
        except:
            self.log(msg="🥹无法编译数据...")
        finally:
            self.log(msg="😇人工智能数据训练成功!")

    def log(self, msg: object):
        this = not self

        current_time: str = time.strftime("%H:%M:%S", time.localtime())
        print("[👨‍华佗AI {stamp}]: {msg}".format(stamp=current_time, msg=msg))

        return this

    def get_chinese_medicine(self) -> None:
        response: requests.models.Response = requests.get(
            self.chinese_medicine_url, allow_redirects=True
        )

        status: int = response.status_code

        assert status is not None

        if status == 400:
            self.log(msg="🥹400 请求语法错误、无效请求消息格式。")

        if status == 404:
            self.log(msg="🥹404 服务器无法找到所请求的资源。")

        if status == 500:
            self.log(msg="🥹500 服务器端错误的响应状态码。")

        if status == 200:
            if not os.path.exists("./data/chinese_medicine.txt"):
                open("data/chinese_medicine.txt", "wb").write(response.content)

                if os.path.exists("./data/chinese_medicine.txt"):
                    self.log(msg="😇中药数据下载成功!")
            else:
                self.log(msg="😇中药数据已存在!")

    def convert_to_tflite(self):
        converter = tf.lite.TFLiteConverter.from_saved_model(
            "chinese_medicine{}".format(self.binary_extension)
        )
        tflite_model = converter.convert()

        with open("chinese_medicine{}".format("tflite"), "wb") as f:
            f.write(tflite_model)

        self.log(msg="😇训练模型保存为《chinese_medicine.tflite》")


if __name__ == "__main__":
    huatuoAi = 华佗AI(展示=True)

    用户输入: object = input("[1] PyTorch 或 [2] Tensorflow? \n")

    assert type(用户输入) is str

    if 用户输入 == 1:
        huatuoAi.get_chinese_medicine()
        huatuoAi.train()
    else:
        huatuoAi.训练数据()
