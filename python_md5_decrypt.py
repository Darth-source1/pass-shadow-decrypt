# @uthor: Shrihan-P 
""" this is a script for decrypt a md5 password on linux from shadow file 
execute this script with root access.
"""

import hashlib
import re

#global variables
user = []
class main:
	
	def __init__():
		pass
	
	def take_md5():
		
		file = open("/etc/shadow", "r")
		#count line for use in loop
		line_count = 0
		for line in file:
			if line != "\n":
				for i in line:
					if i == "$":
						#add local variable x for select the only necesary hash and repeate in case have more users.
						x = []
						x = line.split(sep=":", maxsplit=5)
						temp = x[1]
						x = temp.split(sep="$", maxsplit=3)
						x[2] = x[2] + "$" + x[3]		
						user.append(x[2])
						print(user)
						break
						
					else:
						line_count += 1
		file.close()
		
		
	def search_match():
		dictionary = open("dictionary/list_password.txt", "r")
		for i in dictionary.readlines():
			a = i.strip("\n").encode("utf-8")
			a = hashlib.sha512(a).hexdigest()
			count = 0
			for i in user:
				print(i)
				if a == user[count]:
					print("match")
				elif count < len(user):
					print("no match in user {0}".format(count))
					count += 1
				else:
					pass
			break
		
		
		
		
target = main
target.take_md5()
target.search_match()
		