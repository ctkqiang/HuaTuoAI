# -*- coding: UTF-8 -*-
try:
    import os
    import shutil
    import tensorflow as tf
    import matplotlib.pyplot as plt
    from datetime import datetime
    from colors import green_back
except ImportError:
    raise ImportError("🥹无法安装配件")
finally:
    pass


class 华佗AI:
    def __init__(self, 显示: bool) -> None:
        super(华佗AI, self).__init__()

        plt.rcParams["font.family"] = "Heiti TC"

        assert tf.__version__.startswith("2")

        self.名称: str = "华佗AI"
        self.显示: bool = 显示
        self.图片目录 = "./data/images/"
        self.seed: int = 21
        self.图像高度: int = 32
        self.图像宽度: int = 32
        self.批量大小: int = 20
        self.轴: str | None = "off"
        self.激活函数: str | None = "relu"
        self.中药材料: list | any = ["丁公藤", "金银花", "罗汉果", "人参片"]
        self.优化器: str | None = "adam"
        self.纪元: int = 20

    def 载入数据(self) -> None:
        self.记录信息(信息="[✔] TensorFlow 版本 |>  {}".format(tf.__version__))

        try:
            if os.path.exists(self.图片目录):
                训练数据集 = tf.keras.utils.image_dataset_from_directory(
                    self.图片目录,
                    image_size=(self.图像高度, self.图像宽度),
                    batch_size=self.批量大小,
                )

                if self.显示:
                    plt.figure(figsize=(6, 6))
                    plt.suptitle(self.名称)

                for 图像, 标签 in 训练数据集.take(1):
                    for i in range(9):
                        plt.subplot(3, 3, (i + 1))
                        plt.imshow(图像[i].numpy().astype("uint8"))
                        plt.title(
                            label=self.中药材料[标签[i]], fontsize=15, color="green"
                        )
                        plt.axis(self.轴)

                if self.显示:
                    plt.show()

                模型 = tf.keras.Sequential(
                    [
                        tf.keras.layers.Rescaling(1.0 / 255),
                        tf.keras.layers.Conv2D(32, 1, activation=self.激活函数),
                        tf.keras.layers.MaxPool2D(),
                        tf.keras.layers.Conv2D(32, 1, activation=self.激活函数),
                        tf.keras.layers.MaxPool2D(),
                        tf.keras.layers.Conv2D(32, 1, activation=self.激活函数),
                        tf.keras.layers.MaxPool2D(),
                        tf.keras.layers.Flatten(),
                        tf.keras.layers.Dense(128, activation=self.激活函数),
                    ]
                )

                模型.compile(
                    optimizer=self.优化器,
                    loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
                    metrics=["accuracy"],
                )

                # 这行代码训练模型
                模型.fit(训练数据集, validation_data=训练数据集, epochs=self.纪元)

                try:
                    # 将训练好的模型保存为.pb文件
                    模型文件目录: str = "saved_model"

                    tf.saved_model.save(模型, 模型文件目录)
                except Exception as e:
                    self.记录信息(信息="[x] 训练失败")
                finally:
                    self.记录信息(信息="[✔] 训练成功")

                    编译为tflite: object = input("编译为《.tflite》吗？(是[y]/否[n]) ")

                    if 编译为tflite == "y":
                        pb_模型: str = "saved_model/saved_model.pb"

                        if not os.path.exists("saved_model.pb"):
                            shutil.copy(pb_模型, os.getcwd())

                        输出_tflite_模型: str = "huatuo_ai.tflite"

                        # 将 TensorFlow 模型（.pb）转换为 TensorFlow Lite 模型（.tflite）
                        转换器 = tf.lite.TFLiteConverter.from_saved_model(
                            "saved_model.pb"
                        )
                        tflite_模型 = 转换器.convert()

                        # 将转换后的 TensorFlow Lite 模型保存到文件中
                        with open(输出_tflite_模型, "wb") as f:
                            f.write(tflite_模型)
                    else:
                        return
            else:
                self.记录信息(f"[x] {self.图片目录} 不存在")
        except Exception as e:
            raise e

    def 记录信息(self, 信息: str) -> None:
        现在时间 = datetime.now().strftime("%H:%M:%S")
        print(green_back + f"华佗AI[{现在时间}] {信息}")


if __name__ == "__main__":
    global 图表中显示图片

    在图表中显示图片: object = input("在图表中显示图片吗？(是[y]/否[n]) ")

    if 在图表中显示图片 == "y":
        图表中显示图片 = True
    else:
        图表中显示图片 = False

    华佗_AI = 华佗AI(显示=图表中显示图片)
    华佗_AI.载入数据()
