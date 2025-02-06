import webbrowser
from loader import loader


def test_open_url():
    # 调用 baidu_url 钩子函数
    # 调用 浏览器 访问 baidu_url
    url = loader("baidu_url")
    webbrowser.open_new(url)


if __name__ == '__main__':
    test_open_url()
