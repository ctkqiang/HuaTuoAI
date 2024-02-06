# -*- coding: UTF-8 -*-
try:
    import os
    import tensorflow as tf
    import numpy as np
    import matplotlib
    import matplotlib.pyplot as 图表
    from typing import Tuple
    from datetime import datetime
except ImportError:
    raise ImportError("🥹无法安装配件")
finally:
    pass


class 华佗AI:
    def __init__(self, 展示: bool) -> None:
        super(华佗AI, self).__init__()

        matplotlib.rcParams["font.family"] = "Heiti TC"

        self.名称: str = "华佗AI"
        self.展示: bool = 展示
        self.图片文件 = "./data/images/"
        self.seed: int = 21
        self.图像高度: int = 32
        self.图像宽度: int = 32
        self.批量的大小: int = 20
        self.轴: str | None = "off"
        self.活化: str | None = "relu"
        self.中药材料: list | any = ["丁公藤", "金银花", "罗汉果", "人参片"]
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
                        图表.title(label=self.中药材料[名称[药]], fontsize=10, color="green")
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

        print(f"华佗AI[{目前时间}] {str(信息)}")


if __name__ == "__main__":
    huatuoAi = 华佗AI(展示=True)
    huatuoAi.训练数据()
