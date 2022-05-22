from bs4 import BeautifulSoup

months_converter = {"January": "1", "February": "2", "March": "3", "April": "4", "May": "5", "June": "6", "July": "7",
                    "August": "8", "September": "9", "October": "10", "November": "11", "December": "12"}


def real_time_converter(data_time):
    data_time = data_time.split(" ")
    return f"{data_time[-1]}-{months_converter[data_time[0]]}-{data_time[1].replace(',', '') if not data_time[1][0] == '0' else data_time[1][1]}"


class Generator:
    def __init__(self, original_html, year=2022, date_format="default"):
        self.proceed_data = {}
        if year == 2022:
            temp_var = 0
            proceed_data_model = {"date": "", "confirmed_new": 0, "confirmed_current": 0, "asymptomatic_new": 0,
                                  "asymptomatic_current": 0, "recoveries": 0, "deaths_new": 0}
            simple_data = BeautifulSoup(original_html, features="lxml").find_all('p')[11:]
            for each in range(len(simple_data)):
                if "National Health Commission Update on" in simple_data[each].text:
                    temp_var = each
                    break
            first_data = [each.text for each in simple_data[:temp_var] if not each.text == ""]
            for each in range(0, len(first_data), 5):
                part = first_data[each:each + 5]
                key_time = real_time_converter(part[1])
                if date_format == "default":
                    proceed_data_model["date"] = part[1]
                elif date_format == "chinese":
                    temp_date = part[1].split(" ")
                    temp_date[0] = months_converter[temp_date[0]]
                    temp_date[1] = temp_date[1].replace(",", "")
                    if temp_date[1][0] == "0":
                        temp_date[1] = temp_date[1][1]
                    proceed_data_model["date"] = f"{temp_date[2]}年{temp_date[0]}月{temp_date[1]}日"
                else:
                    raise ValueError("'date_format' parameter must be 'default' or 'chinese'")
                proceed_data_model["confirmed_new"] = int(part[2].split()[1].replace(",", ""))
                proceed_data_model["confirmed_current"] = int(part[2].split()[3].replace(",", ""))
                proceed_data_model["asymptomatic_new"] = int(part[3].split()[1].replace(",", ""))
                proceed_data_model["asymptomatic_current"] = int(part[3].split()[3].replace(",", ""))
                proceed_data_model["recoveries"] = int(part[4].split()[1].replace(",", ""))
                proceed_data_model["deaths_new"] = int(part[4].split()[4].replace(",", ""))
                self.proceed_data[key_time] = proceed_data_model.copy()
            # 补丁(因为网页中有一些数据为0)
            self.proceed_data["2022-3-26"]["confirmed_current"] = 27312
        else:
            raise ValueError("'year' 参数仅为 2022")

    def get_proceed_data(self):
        return self.proceed_data

    def get_proceed_data_sequence(self, data_type):
        return [{each: self.proceed_data[each][data_type]} for each in list(self.proceed_data.keys())][::-1]
