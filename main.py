"""
看似是main，其实就是个调用端（
"""

from modules import updater, generator, renderer
import time
from rich.console import Console

console = Console()
upd = updater.Updater(2022)

data_aspects = {1: "confirmed_new|当日新增确诊", 2: "confirmed_current|当日已有确诊", 3: "asymptomatic_new|当日新增无症状", 4: "asymptomatic_current|当日已有无症状",
           5: "recoveries|当日新增痊愈", 6: "deaths_new|当日新增死亡"}

renderer_aspects = {1: "Pygal", 2: "Matplotlib", 3: "Panda_bokeh"}

render_types = {1: "折线图"}

console.rule("[green]Tracking COVID-19")
data_mode = console.input("是否更新数据？[green]Y/N[white]").lower()
with console.status("正在更新疫情数据..."):
    if data_mode == "y":
        reply = upd.download_html()
    elif data_mode == "n":
        reply = upd.use_backup_html()
    if "online" in reply:
        console.print("[green]已成功更新疫情数据[/]")
    elif "offline" in reply:
        console.print(f"[yellow]更新疫情数据失败，已使用近期的备份数据 | 备份时间:{reply[-1]}[/]")
    elif "backup" in reply:
        console.print(f"[yellow]已直接使用备份的数据 | 备份时间:{reply[-1]}[/]")
year = int(console.input("请选择数据年份:"))
if year == 2022:
    original_html = reply[0]
    console.rule("[green]数据类型")
    for each in range(1, len(data_aspects) + 1):
        print(f"{each}. {data_aspects[each]}")
    aspect = data_aspects[int(console.input("请选择数据类型:"))].split("|")[0]
    with console.status("正在生成疫情数据..."):
        gene = generator.Generator(original_html, year, "chinese")
    time.sleep(0.5)
    generated_data = gene.get_proceed_data_sequence(aspect)
    console.rule("[green]渲染类型")
    for each in range(1, len(renderer_aspects) + 1):
        print(f"{each}. {renderer_aspects[each]}")
    render_selection = renderer_aspects[int(console.input("请选择渲染库:"))]
    if render_selection == "Pygal":
        render = renderer.Pygal_render(generated_data, aspect, True, True)
    elif render_selection == "Matplotlib":
        render = renderer.Matplotlib_render(generated_data, aspect, True, True)
    elif render_selection == "Panda_bokeh":
        render = renderer.Pandas_render(generated_data, aspect, True, True)
    else:
        raise ValueError("渲染库选择错误")
    console.rule("[green]图表类型")
    for each in range(1, len(render_types) + 1):
        print(f"{each}. {render_types[each]}")
    render_selection = render_types[int(console.input("请选择渲染图表类型:"))]
    if render_selection == "折线图":
        render.output_as_line()
else:
    raise ValueError("暂时只支持2022年的数据")
