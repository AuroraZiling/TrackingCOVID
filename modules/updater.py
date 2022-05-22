import time

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
        self.connection_status = "backup"
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
            self.connection_status = "online"
            original_html = requests.get(self.url).text
            if not os.path.exists("data_backup"):
                os.mkdir("data_backup")
            open(f"data_backup/Tracking the Epidemic ({self.year}).html", "w", encoding="utf-8").write(original_html)
            return original_html, self.connection_status
        except ConnectionError:
            reply = self.use_backup_html()
            self.connection_status = "offline"
            if not reply:
                raise UpdaterError('网络连接错误，且没有备份，可能是连接次数过多或网络不好导致的')
            return reply

    def use_backup_html(self):
        if os.path.exists(f"data_backup/Tracking the Epidemic ({self.year}).html"):
            return open(f"data_backup/Tracking the Epidemic ({self.year}).html", "r",
                        encoding="utf-8").read(), self.connection_status, time.ctime(os.path.getmtime(f"data_backup/Tracking the Epidemic ({self.year}).html"))
        return None
