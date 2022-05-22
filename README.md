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

##### 函数 `download_html()`

作用: 下载原HTML文件，并存储至`data_backup`目录下

返回结果: `(original_html, status)`

`original_html`: 原HTML文件

`status`: 获取数据的状态 *online: 在线更新 | offline: 使用了备份*

### 数据处理器 *(Generator.py)*

相关库: `beautifulsoup4`

#### 类: `Generator`

传参:

`original_html`: 原始HTML文本

`year`: 数据年份 *目前仅有2022年*

`date_format`: 日期格式 *默认:default: January 1, 2022 | chinese: 2022年1月1日*

##### 函数 `get_proceed_data(self)`

作用: 获取处理后的数据

返回结果: `proceed_data [dict]`

##### 函数 `get_proceed_data_sequence(self, data_type)`

作用: 筛选字典中的特定数据

`data_type`: 指定数据类型 *参数: confirmed_new confirmed_current asymptomatic_new asymptomatic_current recoveries deaths_new*

返回结果: `proceed_data_sequence [list]`

### 数据分析器 *(Analyzer.py)*

*摸了*

### 数据渲染器 *(Renderer.py)*

#### 函数 `output_as_line(data_sequence, data_type, lib, filename, open_file, chn_trans)`

作用: 将处理后的数据序列和指定的数据类型生成为折线图

`data_sequence`: 处理后的数据序列

`data_type`: 数据的类型

`lib[optional]`: 使用的库 *默认: `pygal` | 支持: `pygal`, `matplotlib`, `pandas_bokeh`*

`filename[optional]`: 导出的文件名 *默认:`output.svg` | 后缀为`.svg`*

`open_file[optional]`: 是否生成数据图后打开文件 *默认:False*

`chn_trans[optional]`: 是否翻译数据类型为中文 *默认:`False`*

## 目标

- [ ] 基本架构完成 *基本能用* **Processing** 
- [ ] 支持2021和2020年的数据 **Planning**
- [ ] 地区支持 **Planning**
- [ ] 多语言支持 **Planning**
- [ ] 日志记录 **Planning**
- [ ] 全GUI支持 **Planning**

### 数据更新器

- [ ] 类化 **Finished**
- [ ] 可调控是否自动更新 **Planning**
- [ ] 显示更新所需时间 **Planning**

### 数据处理器

- [x] 类化 **Processing**
- [ ] 完善原数据的数据类型 **Planning**  

### 数据分析器

- [ ] 趋势分析 **Planning**

### 数据渲染器

- [ ] 类化 **Planning**
- [x] 多库数据渲染 *pygal, matplotlib, pandas_bokeh* **Basically Finished**
- [ ] 渲染参数设置 **Processing**


## 已知问题 

1. 数据网站在2022年3月26日的`confirmed_current`为0 **|已解决|**

替代数据来源(已不可访问): *[中华人民共和国国家卫生健康委员会 截至3月25日24时新型冠状病毒肺炎疫情最新情况](http://www.nhc.gov.cn/xcs/yqfkdt/202203/232b8832229d4918acbcc66e9ce630fb.shtml)*

*[替代数据来源快照](https://baikeshot.cdn.bcebos.com/reference/59764769/dad9b137738560268d1cb30f8ab65e85.png@!reference)*
