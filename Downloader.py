# Coded By : black15
# Date : 2018/05/03
# This Tool Can Download any File (png,jar,iso,pdf,rar,zip....) From Any Web Site for More INFO see the Descrpition 

import os
from time import sleep
import urllib.request
from tqdm import tqdm
from optparse import OptionParser

def welcome():
	print('''\033[1;31m
			  __^__                             __^__
			 ( ___ )---------------------------( ___ )
 			  | / | THE DOWNLOADER WITH PYTHON3 | \ |
 			  |___|                             |___|
			 (_____)---------------------------(_____)''')
	print('\033[1;31m				     by :>: BLACK.15 				\033[1;m')												
def Usage():

	parser = OptionParser('''
	\033[1;31m
			 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
				The Downloader With Python3
			 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
	\033[1;m
Usage:

python3 Downloader.py -u http://www.site.com/download.(exe,pdf,jar,pnj,iso ......)
python3 Downloader.py --url http://www.site.com/download.(exe,pdf,jar,pnj,iso ......)

Example :
	
python3 Downloader.py -u https://wallpapertag.com/wallpaper/full/c/b/4/515350-top-natsu-dragneel-wallpaper-1920x1378.jpg
python3 Downloader.py --url https://wallpapertag.com/wallpaper/full/c/b/4/515350-top-natsu-dragneel-wallpaper-1920x1378.jpg

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
		print('The File Has Been Downloaded :> {}'.format(file_name))
try:
	welcome()
	Usage()
except KeyboardInterrupt :
	sleep(1)
	print("Shutting Down ...")
	sleep(1)
