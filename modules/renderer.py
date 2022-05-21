import os

import pygal

import matplotlib.pyplot as plt

import pandas as pd

import numpy as np

import pandas_bokeh as pb

data_view = pygal.Line()

pd.options.display.notebook_repr_html = False
plt.rcParams['figure.dpi'] = 75
sns.set_theme(style='darkgrid')

chinese_translation = {"confirmed_new": "新增感染", "confirmed_current": "当前感染", "asymptomatic_new": "新增无症状",
                       "asymptomatic_current": "当前无症状", "recoveries": "新增治愈", "deaths_new": "新增死亡"}


def output_as_line(data_sequence, data_type, lib="pygal", filename="output.svg", open_file=False, chn_trans=False):
    t_data_sequence = [list(each.values())[0] for each in data_sequence]
    if chn_trans:
        data_type = chinese_translation[data_type]
    title = f"有关{data_type}的数据(折线图)"
    if lib == "pygal":
        data_view.title = title
        data_view.add(data_type, t_data_sequence)
        data_view.render_to_file(filename)
        if open_file:
            os.startfile(filename)
    elif lib == "matplotlib":
        plt.plot([list(each.keys())[0][5:] for each in data_sequence],
                 [list(each.values())[0] for each in data_sequence])
        plt.show()
    elif lib == "pandas_bokeh":
        data_frame = {"Years": [list(each.keys())[0][5:] for each in data_sequence],
                      data_type: [list(each.values())[0] for each in data_sequence]}
        df = pd.DataFrame(data_frame)
        df.plot_bokeh.line(
            x='Years',
            y=data_type,
            xlabel=data_type,
            ylabel='Years',
            title=title,
            figsize=(800, 500),
            ylim=(5000, 20000),
            zooming=False,
            panning=False,
        )
