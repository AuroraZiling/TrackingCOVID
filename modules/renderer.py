import os
import pygal
import pandas as pd
import pandas_bokeh as pb
import plotly.express as px

chinese_translation = {"confirmed_new": "新增感染", "confirmed_current": "当前感染", "asymptomatic_new": "新增无症状",
                       "asymptomatic_current": "当前无症状", "recoveries": "新增治愈", "deaths_new": "新增死亡"}


class Pygal_render:
    def __init__(self, data_sequence, data_type, open_file=False, chn_trans=False):
        self.data_type = data_type
        self.data_sequence = data_sequence
        self.open_file = open_file
        self.chn_trans = chn_trans
        if not os.path.exists("rendered_data"):
            os.mkdir("rendered_data")

        if type(self.data_sequence) == list:  # 单数据特殊处理
            if chn_trans:
                self.data_type = chinese_translation[self.data_type]
            self.data_sequence_values = [list(each.values())[0] for each in data_sequence]

        self.pygal_data_view = pygal.Line()

    def output_as_line(self, filename="pygal_line.svg", window_title=None):
        self.pygal_data_view.title = f"有关{self.data_type}的数据(折线图)[Pygal]" if not window_title else window_title
        self.pygal_data_view.add(self.data_type, self.data_sequence_values)
        self.pygal_data_view.render_to_file(filename)
        if self.open_file:
            os.startfile(filename)

    def output_as_multiline(self, data_series, filename="pygal_multiline.svg", window_title=None):
        data_types = list(data_series.keys())
        if self.chn_trans:
            title_data_types = [chinese_translation[each] for each in data_types]
        else:
            title_data_types = data_types
        self.pygal_data_view.title = f"有关{','.join(title_data_types)}的数据(多重折线图)[Pygal]" if not window_title else window_title
        if self.chn_trans:
            trans_data = {}
            for each in list(data_series.keys()):
                if each in chinese_translation:
                    trans_data[chinese_translation[each]] = data_series[each]
        else:
            trans_data = data_series
        for each in list(trans_data.keys()):
            self.pygal_data_view.add(each, [i[list(i.keys())[0]] for i in trans_data[each]])
        self.pygal_data_view.render_to_file(filename)
        if self.open_file:
            os.startfile(filename)


class Plotly_render:
    def __init__(self, data_sequence, data_type, open_file=False, chn_trans=False):
        self.data_type = data_type
        self.data_sequence = data_sequence
        self.open_file = open_file
        self.chn_trans = chn_trans
        if not os.path.exists("rendered_data"):
            os.mkdir("rendered_data")

        if type(self.data_sequence) == list:  # 单数据特殊处理
            if chn_trans:
                self.data_type = chinese_translation[self.data_type]
            self.data_sequence_values = [list(each.values())[0] for each in data_sequence]
        if type(self.data_sequence) == list:  # 单数据特殊处理
            self.data_sequence_keys = [list(each.keys())[0][5:] for each in data_sequence]
        else:
            self.data_sequence_keys = [list(each.keys())[0][5:] for each in data_sequence[list(data_sequence.keys())[0]]]

    def output_as_line(self, filename="plotly_line.html", window_title=None):
        window_title = f"有关{self.data_type}的数据(折线图)[Plotly]" if not window_title else window_title
        time_data = pd.DataFrame({
            "年份": self.data_sequence_keys,
            self.data_type: self.data_sequence_values
        })
        fig = px.line(time_data, x="年份", y=[self.data_type], title=window_title)
        fig.show()
        fig.write_html(filename)

    def output_as_multiline(self, data_series, filename="plotly_multiline.html", window_title=None):
        data_types = list(data_series.keys())
        time_data = {"日期": self.data_sequence_keys}
        for data_type in data_types:
            time_data[data_type] = [each[list(each.keys())[0]] for each in data_series[data_type]]
        if self.chn_trans:
            title_data_types = [chinese_translation[each] for each in data_types]
            trans_data = {"日期": self.data_sequence_keys}
            for each in list(time_data.keys()):
                if each in chinese_translation:
                    trans_data[chinese_translation[each]] = time_data[each]
            time_data = trans_data
        else:
            title_data_types = data_types
        window_title = f"有关{','.join(title_data_types)}的数据(多重折线图)[Plotly]" if not window_title else window_title
        fig = px.line(time_data, x="日期", y=time_data, title=window_title)
        fig.show()
        fig.write_html(filename)


class Pandas_render:
    def __init__(self, data_sequence, data_type, open_file=False, chn_trans=False):
        self.data_type = data_type
        self.data_sequence = data_sequence
        self.open_file = open_file
        self.chn_trans = chn_trans
        if not os.path.exists("rendered_data"):
            os.mkdir("rendered_data")

        if type(self.data_sequence) == list:  # 单数据特殊处理
            if chn_trans:
                self.data_type = chinese_translation[self.data_type]
            self.data_sequence_values = [list(each.values())[0] for each in data_sequence]
        if type(self.data_sequence) == list:  # 单数据特殊处理
            self.data_sequence_keys = [list(each.keys())[0][5:] for each in data_sequence]
        else:
            self.data_sequence_keys = [list(each.keys())[0][5:] for each in data_sequence[list(data_sequence.keys())[0]]]

    def output_as_line(self, filename="panda_line.html", window_title=None):
        data_frame = {"年份": self.data_sequence_keys, self.data_type: self.data_sequence_values}
        df = pd.DataFrame(data_frame)
        df.plot_bokeh.line(
            x='年份',
            y=self.data_type,
            xlabel=self.data_type,
            ylabel='年份',
            title=f"有关{self.data_type}的数据(折线图)[Pandas_bokeh]" if not window_title else window_title,
            figsize=(800, 500),
            ylim=(5000, 20000)
        )
        pb.output_file(filename)

    def output_as_multiline(self, data_series, filename="panda_multiline.html", window_title=None):
        data_types = list(data_series.keys())
        time_data = {"日期": self.data_sequence_keys}
        for data_type in data_types:
            time_data[data_type] = [each[list(each.keys())[0]] for each in data_series[data_type]]
        if self.chn_trans:
            title_data_types = [chinese_translation[each] for each in data_types]
            trans_data = {"日期": self.data_sequence_keys}
            for each in list(time_data.keys()):
                if each in chinese_translation:
                    trans_data[chinese_translation[each]] = time_data[each]
            time_data = trans_data
        else:
            title_data_types = data_types
        window_title = f"有关{','.join(title_data_types)}的数据(多重折线图)[Pandas_bokeh]" if not window_title else window_title

        df = pd.DataFrame(time_data)
        df.plot_bokeh.line(
            x='日期',
            y=[each for each in time_data],
            ylabel='日期',
            title=f"有关{title_data_types}的数据(多重折线图)[Pandas_bokeh]" if not window_title else window_title,
            figsize=(800, 500),
            ylim=(5000, 20000)
        )
        pb.output_file(filename)