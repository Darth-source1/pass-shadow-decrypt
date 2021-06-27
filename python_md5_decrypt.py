# @uthor: Shrihan-P 
""" this is a script for decrypt a md5 password on linux from shadow file 
execute this script with root access.
"""

import hashlib, re 
#from os import system, name

#global variables
user = []
selection = ""
file = ""
class main:
	
	def __init__():
		pass
	
	def take_md5(file):
		
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
						target.search_match()
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
			for x in user:
				if a == user[count]:
					print("match in user {0} of {1}".format(count + 1, len(user)))
					print("the password for {0} is {1}".format(count + 1, i))
					count += 1
				elif count < len(user):
					print("no match in user {0} of {1}".format(count + 1, len(user)))
					count += 1
				else:
					break
			break
		
		
		
	def started():
		#Set the source of file
		
		print("hello, welcome to the python_md5_decrypt tool")
		print("select your method")
		
		while True:
			print("1- default 'take from local shadow file'")
			print("2- select my own file")
			selection = input("enter the number of your choice: ")
			if selection == "1":
				file = open("/etc/shadow", "r")
				target.take_md5(file)
				break
			elif selection == "2":
				print("select \n 1- my file is a backup of shadow \n 2- my file is a list of hash")
				while True:
					select_own = input("select 1 or 2: \n")
					if select_own == "1":
						target.my_own_file()
					elif select_own == "2":
						url = input("introduce the url of your file example: /etc/mi_file.txt:s \n ")
						print(url)
						file = open(url, "r")
						for i in file:
							i = i.split(sep="\n")
							i = i[0]
							user.append(i)
						target.search_match()
						break
						
						
						
						
				break
			else:
				pass
				
	def my_own_file():
		url = input("introduce the url of your file example: /etc/mi_file.txt:s \n ")
		print(url)
		file = open(url, "r")
		target.take_md5(file)
		

target = main
target.started()