import pygal


def as_line(data_sequence, data_type):
    view = pygal.Line()
    temp_data_sequence = []
    for each in data_sequence:
        temp_data_sequence.append(list(each.values())[0])
    view.title = f"有关{data_type}的数据 折线图"
    view.add(data_type, temp_data_sequence)
    # view.render_in_browser()
    view.render_to_file('view.svg')

