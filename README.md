# TrackingCOVID

**施工中...**

~~实时~~追踪中国疫情数据

*爬虫、数据分析练手项目（*

## 架构

### 程序入口 *(main.py)*

### 数据更新器 *(Updater.py)*

[数据来源：中国疾病预防控制中心](https://weekly.chinacdc.cn/news/TrackingtheEpidemic.htm)

相关库: `requests`

#### 类: `Updater`

传参: `year` *数据年份(仅支持2022)*

#### 函数 `download_html()`

作用: 下载原HTML文件，并存储至`data_backup`目录下

返回结果: `(original_html, status)`

`original_html`: 原HTML文件

`status`: 获取数据的状态 *online: 在线更新 | offline: 使用了备份*

### 数据处理器 *(Generator.py)*

#### 函数 `clarify_html(original_html, year, date_format)`

作用: 将源HTML文本转换为字典数据

`original_html`: 原始HTML文本

`year`: 数据年份 *目前仅有2022年*

`date_format`: 日期格式 *默认:default: January 1, 2022 | chinese: 2022年1月1日*

返回值: `proceed_data` **类型:dict**

#### 函数 `get_data_sequence(proceed_data, data_type)`

作用: 筛选字典中的特定数据

`proceed_data`: 字典数据

`data_type`: 指定数据类型 *参数: confirmed_new confirmed_current asymptomatic_new asymptomatic_current recoveries deaths_new*

### 数据分析器 *(Analyzer.py)*

*摸了*

### 数据渲染器 *(Renderer.py)*

#### 函数 `output_as_line(data_sequence, data_type, filename, open_file, chn_trans)`

作用: 将处理后的数据序列和指定的数据类型生成为折线图

`data_sequence`: 处理后的数据序列

`data_type`: 数据的类型

`filename[optional]`: 导出的文件名 *默认:`output.svg` | 后缀为`.svg`*

`open_file[optional]`: 是否生成数据图后打开文件 *默认:False*

`chn_trans`: 是否翻译数据类型为中文 *默认:`False`*

## 已知问题 

1. 数据网站在2022年3月26日的`confirmed_current`为0 **|已解决|**

替代数据来源(已不可访问): *[中华人民共和国国家卫生健康委员会 截至3月25日24时新型冠状病毒肺炎疫情最新情况](http://www.nhc.gov.cn/xcs/yqfkdt/202203/232b8832229d4918acbcc66e9ce630fb.shtml)*

*[替代数据来源快照](https://baikeshot.cdn.bcebos.com/reference/59764769/dad9b137738560268d1cb30f8ab65e85.png@!reference)*
