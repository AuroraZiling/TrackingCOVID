from modules import updater
import time
from rich.console import Console
import os

console = Console()

console.rule("[green]Tracking COVID-19")
with console.status("正在更新疫情数据..."):
    time.sleep(0.5)
    reply = updater.get_original_html(2022)
    if "online" in reply:
        console.print("[green]已成功更新疫情数据[/]")
    elif "offline" in reply:
        console.print(f"[yellow]更新疫情数据失败，已使用近期的备份数据 | 备份时间:{time.ctime(os.path.getmtime(reply[-1]))}[/]")
