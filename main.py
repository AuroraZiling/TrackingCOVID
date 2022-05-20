"""
看似是main，其实就是个调用端（
"""

from modules import updater, generator, renderer
import time
from rich.console import Console
import os

console = Console()

console.rule("[green]Tracking COVID-19")
with console.status("正在更新疫情数据..."):
    reply = updater.get_original_html(2022)
    if "online" in reply:
        console.print("[green]已成功更新疫情数据[/]")
    elif "offline" in reply:
        console.print(f"[yellow]更新疫情数据失败，已使用近期的备份数据 | 备份时间:{time.ctime(os.path.getmtime(reply[-1]))}[/]")
original_html = reply[0]
with console.status("正在生成疫情数据..."):
    reply = generator.clarify_html(original_html, 2022, "chinese")
reply = generator.get_data_sequence(reply, "confirmed_current")
renderer.as_line(reply, "confirmed_current")
