import requests
import json
from pprint import pprint
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}
# 获取歌曲信息
def get_mp3_url():
    url='http://musicapi.taihe.com/v1/restserver/ting?method=baidu.ting.song.playAAC&format=jsonp&songid=242078437&from=web'
    response = requests.get(url,headers=headers)

    # pprint(response.json())
    # 将json数据赋值给data
    data=response.json()

    # 提取数据
    song_url = data['bitrate']['file_link']
    song_name = data['songinfo']['title']
    # 保存歌曲
    with open(song_name+'.mp3','wb')as f:
        f.write(requests.get(song_url).content)
    return song_url,song_name
print(get_mp3_url())

