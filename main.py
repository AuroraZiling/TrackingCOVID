"""
看似是main，其实就是个调用端（
"""

from modules import updater, generator, renderer
import time
from rich.console import Console
import os

console = Console()
upd = updater.Updater(2022)

console.rule("[green]Tracking COVID-19")
with console.status("正在更新疫情数据..."):
    reply = upd.download_html()
    if "online" in reply:
        console.print("[green]已成功更新疫情数据[/]")
    elif "offline" in reply:
        console.print(f"[yellow]更新疫情数据失败，已使用近期的备份数据 | 备份时间:{time.ctime(os.path.getmtime(reply[-1]))}[/]")
year = int(console.input("请选择数据年份:"))
if year == 2022:
    original_html = reply[0]
    aspect = console.input("请选择数据类型:")
    with console.status("正在生成疫情数据..."):
        generated_data = generator.clarify_html(original_html, year, "chinese")
    time.sleep(0.5)
    generated_data = generator.get_data_sequence(generated_data, aspect)
    renderer.output_as_line(generated_data, aspect, "output.svg", True, True)
else:
    raise ValueError("暂时只支持2022年的数据")
