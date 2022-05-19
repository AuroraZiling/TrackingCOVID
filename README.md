# TrackingCOVID

~~实时~~追踪中国疫情数据

*爬虫、数据分析练手项目（*

## 架构

### 程序入口 *(main.py)*

### 数据更新器 *(Updater.py)*

[数据来源：中国疾病预防控制中心](https://weekly.chinacdc.cn/news/TrackingtheEpidemic.htm)

相关库：`requests`

### 数据处理器 *(Generator.py)*

#### 函数 `clarify_html(original_html, year, date_format)`

`original_html`: 原始HTML文本

`year`: 数据年份 *目前仅有2022年*

`date_format`: 日期格式 *默认:default: January 1, 2022 | chinese: 2022年1月1日*

返回值: `proceed_data` **类型:dict**

### 数据分析器 *(Analyzer.py)*

*摸了*

### 数据渲染器 *(Renderer.py)*

*摸了*