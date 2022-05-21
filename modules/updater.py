import requests
import os


class UpdaterError(Exception):
    pass


class Updater:
    def __init__(self, year):
        self.data_url_2022 = 'https://weekly.chinacdc.cn/news/TrackingtheEpidemic.htm'
        self.data_url_2021 = 'https://weekly.chinacdc.cn/news/TrackingtheEpidemic2021.htm'
        self.data_url_2020 = 'https://weekly.chinacdc.cn/news/TrackingtheEpidemic2020.htm'
        self.year = year
        if self.year == 2022:
            self.url = self.data_url_2022
        elif self.year == 2021:
            raise UpdaterError('暂无2021年数据')
            # self.url = self.data_url_2021
        elif self.year == 2020:
            raise UpdaterError('暂无2020年数据')
            # self.url = self.data_url_2020
        else:
            raise UpdaterError('请输入正确的年份(2022)')

    def download_html(self):
        try:
            original_html = requests.get(self.url).text
            if not os.path.exists("data_backup"):
                os.mkdir("data_backup")
            open(f"data_backup/Tracking the Epidemic ({self.year}).html", "w", encoding="utf-8").write(original_html)
            return original_html, "online"
        except ConnectionError:
            if os.path.exists(f"data_backup/Tracking the Epidemic ({self.year}).html"):
                return open(f"data_backup/Tracking the Epidemic ({self.year}).html", "r",
                            encoding="utf-8").read(), "offline"
            raise ConnectionError('网络连接错误，且没有备份，可能是连接次数过多或网络不好导致的')