import requests
class news:
    def __init__(self):
        print("-")
    def get_news():
        """获取金山词霸每日一句，英文和翻译"""
        url = "http://open.iciba.com/dsapi/"
        r = requests.get(url)
        content = r.json()['content']
        note = r.json()['note']
        return content, note

    if __name__ == "__main__":
        print(get_news())