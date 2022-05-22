import os

import pygal

import matplotlib.pyplot as plt

import pandas as pd

import numpy as np

import pandas_bokeh as pb


chinese_translation = {"confirmed_new": "新增感染", "confirmed_current": "当前感染", "asymptomatic_new": "新增无症状",
                       "asymptomatic_current": "当前无症状", "recoveries": "新增治愈", "deaths_new": "新增死亡"}

class Pygal_render:
    def __init__(self, data_sequence, data_type, open_file=False, chn_trans=False):
        self.data_type = data_type
        self.data_sequence = data_sequence
        self.open_file = open_file
        self.chn_trans = chn_trans
        if os.path.exists("rendered_data"):
            os.mkdir("rendered_data")

        if chn_trans:
            self.data_type = chinese_translation[self.data_type]

        self.data_sequence_values = [list(each.values())[0] for each in data_sequence]

        self.pygal_data_view = pygal.Line()

    def output_as_line(self, filename="pygal_line.svg", window_title=None):
        self.pygal_data_view.title = f"有关{self.data_type}的数据(折线图)[Pygal]" if not window_title else window_title
        self.pygal_data_view.add(self.data_type, self.data_sequence)
        self.pygal_data_view.render_to_file(filename)
        if self.open_file:
            os.startfile(filename)


class Matplotlib_render:
    def __init__(self, data_sequence, data_type, open_file=False, chn_trans=False):
        self.data_type = data_type
        self.data_sequence = data_sequence
        self.open_file = open_file
        self.chn_trans = chn_trans
        if os.path.exists("rendered_data"):
            os.mkdir("rendered_data")

        if chn_trans:
            self.data_type = chinese_translation[self.data_type]

        self.data_sequence_values = [list(each.values())[0] for each in data_sequence]
        self.data_sequence_keys = [list(each.keys())[0][5:] for each in data_sequence]

    def output_as_line(self, filename="matplotlib_line.png", window_title=None):
        plt.title(f"有关{self.data_type}的数据(折线图)[Matplotlib]") if not window_title else window_title
        plt.plot(self.data_sequence_keys, self.data_sequence_values)
        plt.show()
        plt.savefig(filename)


class Pandas_render:
    def __init__(self, data_sequence, data_type, open_file=False, chn_trans=False):
        self.data_type = data_type
        self.data_sequence = data_sequence
        self.open_file = open_file
        self.chn_trans = chn_trans
        if os.path.exists("rendered_data"):
            os.mkdir("rendered_data")

        if chn_trans:
            self.data_type = chinese_translation[self.data_type]

        self.data_sequence_values = [list(each.values())[0] for each in data_sequence]
        self.data_sequence_keys = [list(each.keys())[0][5:] for each in data_sequence]

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
