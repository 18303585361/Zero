from urllib import request
'''
使用 urllib.request 请求一个网页内容，并把内容打印出来
'''

if __name__ == '__main__':

    url = 'https://www.28haoma.com/yuce/1/2.html'
    # 打开相应的 url 并把相应页面作为返回
    res = request.urlopen(url)

    # 把返回的结果读取出来
    # 读取出来的内容类型为 bytes
    html = res.read()

    # 如果想把 byte 内容转换成字符串，需要解码
    html = html.decode('utf-8')
    print(html)