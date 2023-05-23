try:
    import os
    import requests
    import pandas as pd
    from bs4 import BeautifulSoup
except:
    raise "无法安装配件"


class HuaTuoAI:
    def __init__(self):
        self.chinese_medicine_url: str = "https://ylbz.yn.gov.cn/index.php?c=page&id=22"

    def train(self):
        pass  # train Images

    def scrape_chinese_medicine(self) -> None:
        global table_name

        response: requests.models.Response = requests.get(self.chinese_medicine_url)
        status: int = response.status_code

        assert status is not None

        if status == 400:
            raise "400 请求语法错误、无效请求消息格式。"

        if status == 404:
            raise "404 服务器无法找到所请求的资源。"

        if status == 500:
            raise "500 服务器端错误的响应状态码。"

        if status == 200:
            body: bytes = response.content
            soup: BeautifulSoup = BeautifulSoup(body, "html.parser")

            assert type(soup) == BeautifulSoup
            assert soup is not None

            # 在网站上查找 "table" 的数量
            for table in soup.find_all("table"):
                assert table is not None  # "table" 不可为空
                table_name = table.get("class")
                print(table_name)

            # 🤪🤪🤪🤪 不需要拉数据了，我在其他地方得到了此数据。


if __name__ == "__main__":
    huatuoai = HuaTuoAI()

    if not os.path.exists("./data/chinese_medicine.txt"):
        huatuoai.scrape_chinese_medicine()

    huatuoai.train()
