import requests

url = "http://www.baidu.com/s"
params = {
    "wd": "美女"
}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"}
response = requests.get(url, headers=headers, params=params)
data = response.content.decode("utf-8")
with open("16_baidu.html", "w", encoding="utf-8") as f:
    f.write(data)
