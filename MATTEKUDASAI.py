# -*- coding: utf-8 -*-
import sys , requests, re, random, string
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import init 
init(autoreset=True)
fr  =   Fore.RED
fg  =   Fore.GREEN

banner = '''{}

 $$$$$$\ $$$$$$$$\  $$$$$$\  
$$  __$$\\__$$  __|$$  __$$\ 
$$ /  \__|  $$ |   $$ /  $$ |
$$$$$$$\    $$ |   \$$$$$$$ |
$$  __$$\   $$ |    \____$$ |
$$ /  $$ |  $$ |   $$\   $$ |
 $$$$$$  |  $$ |   \$$$$$$  |
 \______/   \__|    \______/ 
 

 
          Telegram: https://t.me/teamanonforce
                  Owner: @Professor6T9 
\n'''.format(fg)
print banner
requests.urllib3.disable_warnings()

try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')

def ran(length):
	letters = string.ascii_lowercase
	return ''.join(random.choice(letters) for i in range(length))

Pathlist = ['/go.php','/wp-content/themes/too.php','/wp-includes/assets/winnner.php']
class EvaiLCode:
	def __init__(self):

		self.headers = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36'}

	
	def URLdomain(self, site):

		if site.startswith("http://") :
			site = site.replace("http://","")
		elif site.startswith("https://") :
			site = site.replace("https://","")
		else :
			pass
		pattern = re.compile('(.*)/')
		while re.findall(pattern,site):
			sitez = re.findall(pattern,site)
			site = sitez[0]
		return site
		
		
	def checker(self, site):
		try:
			
			url = "http://" + self.URLdomain(site)
			for Path in Pathlist:
				check = requests.get(url + Path, headers=self.headers, verify=False, timeout=25).content
				if('<title>MATTEKUDASAI</title>' in check):
					print('[x] {} --> {}[Vuln]').format(url, fg)
					open('Vuln.txt','a').write(url + Path + "\n")
					break
				else:
					print('[x] {} --> {}[Not Vuln]').format(url, fr)
					
		except:
			pass

Control = EvaiLCode()	
def Professor6T9(site):
	try:
		Control.checker(site)
	except:
		pass
mp = Pool(100)
mp.map(Professor6T9, target)
mp.close()
mp.join()
input("TASK COMPLETED")