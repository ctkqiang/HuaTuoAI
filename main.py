try:
    import os
    import requests
    from bs4 import BeautifulSoup
except:
    raise "无法安装配件"


class HuaTuoAI:
    def __init__(self):
        pass

    def train(self):
        pass  # train Images

    @staticmethod
    def scrape_chinese_medicine() -> None:
        url: str = "https://ylbz.yn.gov.cn/index.php?c=page&id=22"

        response: object = requests.get(url)
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
            

if __name__ == "__main__":
    huatuoai = HuaTuoAI()

    if not os.path.exists("./data/chinese_medicine.csv"):
        huatuoai.scrape_chinese_medicine()

    huatuoai.train()
