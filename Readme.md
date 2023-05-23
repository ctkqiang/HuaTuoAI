# 华佗AI
本存储库包含一个针对中药的人工智能图像分类系统。该项目的目标是通过输入图像准确识别和分类各种中草药和成分。

### 功能特点
- **图像分类**：该项目的核心功能是图像分类模型，利用深度学习技术对中草药和成分进行分类。模型使用了一种称为卷积神经网络（Convolutional Neural Network，CNN）的算法。具体而言，模型通过一系列卷积层、池化层和全连接层来提取图像中的特征，并利用softmax函数将图像分为不同的类别。模型的数学表示如下：
```latex
\begin{equation}
(f * g)(n) = \sum_{m = -\infty}^{\infty} f(m) \cdot g(n - m)
\end{equation}
```

<img src="https://raw.githubusercontent.com/johnmelodyme/HuaTuoAI/main/assets/imageclassificationformual.png" style="float: left; margin-right: 10px;" />

> 在这个公式中，`(f * g)(n)` 表示在位置 `n` 对两个函数 `f` 和 `g` 进行卷积操作的结果。符号 `*` 表示卷积操作，
求和符号 `\sum` 对 `m` 的范围进行求和计算。该公式在每个 `m` 值处将 `f(m)` 和 `g(n - m)` 相乘，并将它们相加，
以得到卷积结果 `(f * g)(n)`。


### 配置
```bash
pip3 install -r requirements.txt
```

### 用法

```bash
python3 main.py
```