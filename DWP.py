# Coded By : black15
# Date : 2018/05/03
# This Tool Can Download any File (png,jar,iso,pdf,rar,zip....) From Any Web Site for More INFO see the Descrpition 

import os,sys
from time import sleep
import urllib.request
from tqdm import tqdm
from optparse import OptionParser
import colorama
from colorama import Fore, Style

def slowprints1(slow):
        for slowprint in slow +"\n":
            sys.stdout.write(slowprint)
            sys.stdout.flush()
            sleep(3./90)

def welcome():
	print('''\033[1;31m
			  __^__                             __^__
			 ( ___ )---------------------------( ___ )
 			  | / | THE DOWNLOADER WITH PYTHON3 | \ |
 			  |___|                             |___|
			 (_____)---------------------------(_____)''')
	slowprints1('\033[1;31m				     BY : > B14CK_DZ 				\033[1;m')												
def Usage():

	parser = OptionParser('''
	\033[1;31m
			 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

				DOWNLOAD FILES WITH PYTHON
			 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
	\033[1;m
Usage:

python3 DWP.py -u http://www.site.com/file.(exe,pdf,jar,pnj,iso..)
python3 DWP.py --url http://www.site.com/file.(exe,pdf,jar,pnj,iso..)
	''')


	parser.add_option('-u','--url',dest='my_url',type='string')

	(options,args) = parser.parse_args()

	if options.my_url == None:
		print(parser.usage)

	else :
	
		URL = options.my_url
		urlopen = urllib.request.urlopen(URL)
		file_name = URL.split('/')[-1]
		openfile = open(file_name,'wb')
		block_size = 1000
		file_size = int(urlopen.headers['Content-Length'])
		for i in tqdm(range(file_size)):
			Buffer = urlopen.read(block_size)
			i = i + block_size
			openfile.write(Buffer)
		openfile.close()
		print(Fore.GREEN + '[*] The File Has Been Downloaded :> {}'.format(file_name))
try:
	welcome()
	Usage()
except KeyboardInterrupt :
	sleep(1)
	print(Fore.RED + "\n[!] Shutting Down ...\n")
	sleep(1)
except ValueError:
	sleep(1)
	print(Fore.RED + "\n[!] Check URL Again ")
	sleep(1)