import requests

url = 'https://hls.videocc.net/f8f97d17d0/d/f8f97d17d0a21f1a1d84d214c5dcbfdd_1.key'
res = requests.get(url)
print(res.text)
print(res.__dict__)