import unittest
from unittest.mock import patch, MagicMock
import 华佗AI


class Test华佗AI(unittest.TestCase):
    def setUp(self):
        self.huatuoAi = 华佗AI(展示=True)

    @patch("华佗AI.tf")
    def test_训练数据(self, mock_tf):
        mock_image_dataset = MagicMock()
        mock_image_dataset_from_directory = MagicMock(return_value=mock_image_dataset)
        mock_tf.keras.utils.image_dataset_from_directory = (
            mock_image_dataset_from_directory
        )

        self.huatuoAi.训练数据()

        mock_image_dataset_from_directory.assert_called_with(
            self.huatuoAi.图片文件,
            image_size=(self.huatuoAi.图像高度, self.huatuoAi.图像宽度),
            batch_size=self.huatuoAi.批量的大小,
        )
        self.assertTrue(mock_image_dataset.take.called)
        self.assertTrue(mock_image_dataset.compile.called)
        self.assertTrue(mock_image_dataset.fit.called)

    @patch("builtins.print")
    @patch("华佗AI.datetime")
    def test_记录(self, mock_datetime, mock_print):
        mock_now = MagicMock()
        mock_now.strftime.return_value = "12:00:00"
        mock_datetime.now.return_value = mock_now

        self.huatuoAi.记录("测试信息")

        mock_datetime.now.assert_called_once()
        mock_print.assert_called_with("华佗AI[12:00:00] 测试信息")


if __name__ == "__main__":
    unittest.main()
