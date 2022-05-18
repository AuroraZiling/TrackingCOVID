from bs4 import BeautifulSoup


def clarify_html(original_html):  # 目前仅适用于2022年的数据
    temp_var = 0
    simple_data = BeautifulSoup(original_html, features="lxml").find_all('p')[11:]
    for each in range(len(simple_data)):
        if "National Health Commission Update on" in simple_data[each].text:
            temp_var = each
            break
    simple_data = [each.text for each in simple_data[:temp_var]]
    print(simple_data)
    # Todo: 转化为字典，以天为key，数据为value存在list里面
