import data, requests, sys, os, rich
import webbrowser
import time
import json
from rich.progress import track

def show_sv(jstatus, item):
    rich.print(f"[yellow italic]server #{item}:[/]")
    rich.print(f"  online: {jstatus["status"][item]["online"]}")
    rich.print(f'  name: "{jstatus["status"][item]["name"]}"')
    try:
        jstatus["status"][item]["uptime"]
        rich.print(f"  uptime: {jstatus["status"][item]["uptime"]}")
    except:
        pass
    try:
        jstatus["status"][item]["clients"]
        rich.print(f"  clients: {jstatus["status"][item]["clients"]}")
    except:
        pass
    try:
        jstatus["status"][item]["mspt"]
        rich.print(f"  mspt: {jstatus["status"][item]["mspt"]}")
    except:
        pass
    rich.print(f'  code: "{jstatus["status"][item]["code"]}"')
    rich.print(f'  host: "{jstatus["status"][item]["host"]}"')
    try:
        jstatus["status"][item]["hidden"]
        rich.print(f"  hidden: {jstatus["status"][item]["hidden"]}")
    except:
        pass
def check_load():
    global jstatus, jclientCount
    print("Loading: ")
    """
    print("  Check status of arras.io:")
    print("    Main: ", end = "")
    arras = requests.get("https://arras.io/")
    if arras.status_code == 200:
        rich.print("[green]OK[/]✅")
    else:
        rich.print("[red]Bad[/]❌")
        sys.exit()
    """
    print("  Load data of arras.io:")
    print('    "status": ', end = "")
    status = requests.get("https://fsas4nob1arq32ll.uvwx.xyz:2222/status")
    if status.status_code == 200:
        jstatus =  status.json()
        rich.print("[green]OK[/]✅")
    else:
        rich.print("[red]Bad[/]❌")
        sys.exit()
    print('    "clientCount": ', end = "")
    clientCount = requests.get("https://fsas4nob1arq32ll.uvwx.xyz:2222/clientCount")
    if clientCount.status_code == 200:
        jclientCount = clientCount.json()
        rich.print("[green]OK[/]✅")
    else:
        rich.print("[red]Bad[/]❌")
        sys.exit()
print(data.WC)
jstatus = {}
jclientCount = {}
check_load()
commnad = ""
title, value = commnad.split(" ") if len(commnad.split()) > 1 else commnad, ""
while title != "/exit":
    commnad = input("T$ ")
    title = commnad.split(" ")[0]
    try:
        value = commnad.split(" ")[1:]
        value = " ".join(value)
    except IndexError:
        value = ""
    lvalue = value.split(" ") if value != "" else [""]
    if title == "/view":
        if lvalue[0] == "-asv":
            os.system("cls")
            count = 0
            for item in jstatus["status"]:
                show_sv(jstatus, item)
                count += 1
            rich.print(f"[green]arras.io have {count} server![/]")
        elif lvalue[0] == "-clc":
            os.system("cls")
            rich.print(f"client count: {jclientCount}")
    elif title == "/search":
        os.system("cls")
        temp = []
        have = False
        count = 0
        a = 0
        for item in jstatus["status"]:
            if item.count(lvalue[0]) > 0:
                show_sv(jstatus, item)
                have = True
                count += 1
            a += 1
        if not have:
            rich.print("[yellow]Not have server look like that![/]")
        else:
            rich.print(f"[green]Have {count}/{a} server look like that![/]")
    elif title == "/filter":
        def ft(value, jstatus, item):
            re = value
            re = re.replace("online", f"{jstatus["status"][item]["online"]}")
            re = re.replace("name", f"{jstatus["status"][item]["name"]}")
            try:
                jstatus["status"][item]["uptime"]
                re = re.replace("uptime", f"{jstatus["status"][item]["uptime"]}")
            except:
                re = re.replace("uptime", f"0")
            try:
                jstatus["status"][item]["clients"]
                re = re.replace("clients", f"{jstatus["status"][item]["clients"]}")
            except:
                re = re.replace("clients", f"0")
            try:
                jstatus["status"][item]["mspt"]
                re = re.replace("mspt", f"{jstatus["status"][item]["mspt"]}")
            except:
                re = re.replace("mspt", f"0")
            re = re.replace("code", f"{jstatus["status"][item]["code"]}")
            re = re.replace("host", f"{jstatus["status"][item]["host"]}")
            try:
                jstatus["status"][item]["hidden"]
                re = re.replace("hidden", f"{jstatus["status"][item]["hidden"]}")
            except:
                re = re.replace("hidden", f"0")
            return re
        os.system("cls")
        temp = []
        have = False
        count = 0
        a = 0
        y = " ".join(lvalue)
        for item in jstatus["status"]:
            try:
                eval(ft(y, jstatus, item))
                if ("true" if (eval(ft(y, jstatus, item)) != 1 or eval(ft(y, jstatus, item)) != 0) and eval(ft(y, jstatus, item)) == True else "false") == "true":
                    show_sv(jstatus, item)
                    have = True
                    count += 1
                a += 1
            except:
                rich.print("[red]Your filter math is not corret[/]")
                break
        if not have:
            rich.print("[yellow]Not have server look like that![/]")
        else:
            rich.print(f"[green]Have {count}/{a} server look like that![/]")
    elif title == "/join":
        if lvalue[0] == "-j":
            for item in track(lvalue[1:], description="Processing join server..."):
                rich.print(f"  -> join https://arras.io/{item}")
                webbrowser.open(f"https://arras.io/{item}")
        elif lvalue[0] == "-sj":
            for i in track(range(int(lvalue[1])), description="Processing spam join server..."):
                rich.print(f"  -> spam {i} https://arras.io/{lvalue[2]}")
                webbrowser.open(f"https://arras.io/{lvalue[2]}")
    elif title == "/stats":
        os.system("cls")
        total_servers = len(jstatus["status"])
        online_servers = sum(1 for item in jstatus["status"] if jstatus["status"][item]["online"])
        total_clients = sum(jstatus["status"][item]["clients"] for item in jstatus["status"] if "clients" in jstatus["status"][item])

        rich.print(f"[cyan]Arras.io Statistics:[/]")
        rich.print(f"  Total servers: [yellow]{total_servers}[/]")
        rich.print(f"  Online servers: [green]{online_servers}[/]")
        rich.print(f"  Total players: [blue]{total_clients}[/]")

    elif title == "/sort":
        os.system("cls")
        sorted_servers = sorted(jstatus["status"].items(), key=lambda x: x[1].get("clients", 0), reverse=True)
        for item, data in sorted_servers:
            show_sv(jstatus, item)
    elif title == "/export":
        with open(f"{lvalue[0]}.", "w", enconding = "utf-8") as f:
            json.dump(jstatus, f, indent=4)
        rich.print(f"[green]Dữ liệu đã được lưu vào {lvalue[0]}.json[/]")
    elif title == "/refesh":
        if lvalue[0] == "-a":
            check_load()

            

