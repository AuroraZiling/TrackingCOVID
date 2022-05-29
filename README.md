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

传参: `year: int` *数据年份(仅支持2022)*

##### 函数 `download_html()`

作用: 下载原HTML文件，并存储至`data_backup`目录下

返回结果: `(original_html, status): tuple`

`original_html: str`: 原HTML文件

`status: str`: 获取数据的状态 *online: 在线更新 | offline: 因为离线而使用备份*

##### 函数 `use_backup_html()`

作用: 使用备份的HTML文件

返回结果: `(original_html, status, backup_time): tuple`

`original_html: str`: 原HTML文件

`status: str`: 获取数据的状态 *backup: 使用了备份*

`backup_time: str`: HTML文件的备份时间

### 数据处理器 *(Generator.py)*

相关库: `beautifulsoup4`

#### 类: `Generator`

传参:

`original_html: str`: 原始HTML文本

`year: int`: 数据年份 *目前仅有2022年(默认)*

`date_format: str`: 日期格式 *默认:default: January 1, 2022 | chinese: 2022年1月1日*

##### 函数 `get_proceed_data(self)`

作用: 获取处理后的数据

返回结果: `proceed_data: dict`

##### 函数 `get_proceed_data_sequence(self, data_type: str)`

作用: 筛选字典中的特定数据

`data_type`: 指定数据类型 *参数: confirmed_new confirmed_current asymptomatic_new asymptomatic_current recoveries deaths_new*

返回结果: `proceed_data_sequence: list`

##### 函数 `get_proceed_data_sequences(self, data_types: list)`

作用: 筛选字典中的多特定数据

`data_types`: 指定多数据类型 *参数: confirmed_new confirmed_current asymptomatic_new asymptomatic_current recoveries deaths_new*

返回结果: `proceed_data_sequences: dict`

### 数据分析器 *(Analyzer.py)*

*摸了*

### 数据渲染器 *(Renderer.py)*

#### 类: `Pygal_render`, `Plotly_render`, `Pandas_render`

##### 函数 `output_as_line(self, filename, window_title)`

作用: 将处理后的数据序列和指定的数据类型生成为折线图

`filename[optional]`: 导出的文件名

`window_title[optional]`: 是否使用自定义标题 *默认:`None`*

*无返回结果，但会在目录下生成文件*

##### 函数 `output_as_multiline(self, data_series, filename, window_title)`

作用: 将处理后的多重数据序列和指定的多重数据类型生成为多重折线图

`data_series`: 处理后的多重数据序列

`filename[optional]`: 导出的文件名

`window_title[optional]`: 是否使用自定义标题 *默认:`None`*

*无返回结果，但会在目录下生成文件*

## 目标

- [ ] 基本架构完成 *基本能用* **Processing** 
- [ ] 支持2021和2020年的数据 **Planning**
- [ ] 地区支持 **Planning**
- [ ] 多语言支持 **Planning**
- [ ] 日志记录 **Planning**
- [ ] 全GUI支持 **Processing**

### 数据更新器

- [x] 类化 **Finished**
- [x] 可直接使用备份数据 **Finished**
- [ ] 显示更新所需时间 **Planning**

### 数据处理器

- [x] 类化 **Processing**
- [ ] 完善原数据的数据类型 **Planning**  

### 数据分析器

- [ ] 趋势分析 **Planning**

### 数据渲染器

- [x] 类化 **Finished**
- [x] 多库数据渲染 *pygal, plotly, pandas_bokeh* **Basically Finished**
- [ ] 渲染参数设置 **Planning**

#### 图的类型

- [x] 单折线图 **Finished**
- [x] 多折线图 **Finished**

## 已知问题 

1. 数据网站在2022年3月26日的`confirmed_current`为0 **|已解决|**

替代数据来源(已不可访问): *[中华人民共和国国家卫生健康委员会 截至3月25日24时新型冠状病毒肺炎疫情最新情况](http://www.nhc.gov.cn/xcs/yqfkdt/202203/232b8832229d4918acbcc66e9ce630fb.shtml)*

*[替代数据来源快照](https://baikeshot.cdn.bcebos.com/reference/59764769/dad9b137738560268d1cb30f8ab65e85.png@!reference)*
