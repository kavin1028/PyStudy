# 第一步，导入第三方库  网络上请求数据
# 第二部  获取目标网页
# 第三步  解析目标网页
# 第四部  下载目标网页数据


# 导入第三方库
import requests
from urllib.parse import urlencode  # a=1&b=2这样一个数据格式
import os
from hashlib import md5


# 2定义一个函数 请求网站数据
def get_page(offset):
    # 2.1定义参数的属性
    # 属性是键值对定义一个字典
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '车模',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab'

    }
    # 2.2 拼接URL https://www.toutiao.com/search_content/?offset=80&format=json&keyword==%E8%BD%A6%E6%A8%A1&autoload=true&count=20&cur_tab=1&from=search_tab&pd=synthesis
    url = 'https://www.toutiao.com/search_content/?' + urlencode(params)

    # 2.3 请求这个链接
    response = requests.get(url)

    # 2.4 如果返回的状态码为200
    if response.status_code == 200:
        return response.json()


# 第三步 解析
# 3 定义一个函数目的 实现一个解析的方法
def get_images(json):
    # 获取数据
    data = json.get('data')

    if data:
        # 变例得到image_list url 和title
        for item in data:
            image_list = item.get('image_list')
            source = item.get('source')

            if image_list:
                for image in image_list:
                    # 构造一个生成器 将图片连接和属性一起返回
                    yield {
                        'image': image.get('url'),
                        'source': source
                    }


# 第四步下载数据
# 定义函数 实现保存图片的方法 title作为文件夹名称 图片名称以一个32为16进制命名

def save_image(item):
    if not os.path.exists(item.get('source')):
        os.mkdir(item.get('source'))

    # 4.1 获取连接
    local_image_url = item.get('image')

    # 4.2 请求
    response = requests.get('http:' + local_image_url)

    if response.status_code == 200:
        file_path = '{0}/{1}.{2}'.format(item.get('source'), md5(response.content).hexdigest(), 'jpg')
        # {0}:文件夹的名称 {1}:图片名 {2}: 图片的格式
        if not os.path.exists(file_path):
            with open(file_path, 'wb')as f:
                f.write(response.content)


# 5
def main(offset):
    # 5.1 先调用get_page
    json = get_page(offset)

    # 5.2 遍历数据打印标题
    for item in get_images(json):
        print(item)
        save_image(item)


# 6 启动程序
if __name__ == '__main__':
    main(80)
