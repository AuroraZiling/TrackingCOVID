import os

import pygal

data_view = pygal.Line()

chinese_translation = {"confirmed_new": "新增感染", "confirmed_current": "当前感染", "asymptomatic_new": "新增无症状",
                       "asymptomatic_current": "当前无症状", "recoveries": "新增治愈", "deaths_new": "新增死亡"}


def output_as_line(data_sequence, data_type, filename="output.svg", open_file=False, chn_trans=False):
    data_sequence = [list(each.values())[0] for each in data_sequence]
    data_view.title = f"有关{data_type if not chn_trans else chinese_translation[data_type]}的数据 折线图"
    data_view.add(data_type if not chn_trans else chinese_translation[data_type], data_sequence)
    data_view.render_to_file(filename)
    if open_file:
        os.startfile(filename)
