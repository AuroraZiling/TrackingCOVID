import requests
import os

data_url_2022 = 'https://weekly.chinacdc.cn/news/TrackingtheEpidemic.htm'
data_url_2021 = 'https://weekly.chinacdc.cn/news/TrackingtheEpidemic2021.htm'
data_url_2020 = 'https://weekly.chinacdc.cn/news/TrackingtheEpidemic2020.htm'


def get_original_html(year=2022):
    if year == 2022:
        url = data_url_2022
    elif year == 2021:
        # url = data_url_2021
        raise ValueError('暂未开发2021年疫情数据分析')
    elif year == 2020:
        # url = data_url_2020
        raise ValueError('暂未开发2020年疫情数据分析')
    else:
        raise ValueError('数据的年份必须为2022')
    try:
        original_html = requests.get(url).text
        open(f"Tracking the Epidemic ({year}).html", "w", encoding="utf-8").write(original_html)
        return original_html, "online", f"Tracking the Epidemic ({year}).html"
    except ConnectionError:
        if os.path.exists(f"Tracking the Epidemic ({year}).html"):
            return open(f"Tracking the Epidemic ({year}).html", "r", encoding="utf-8").read(), "offline", f"Tracking the Epidemic ({year}).html"
        raise ConnectionError('网络连接错误，且没有最近备份，可能是连接次数过多或网络不好导致的')
