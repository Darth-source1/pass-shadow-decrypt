# @uthor: Shrihan-P 
""" this is a script for decrypt a md5 password on linux from shadow file 
execute this script with root access.
"""
#global variables

user = []
class md5_decrypt:
	
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
						x = line.split(sep=":", maxsplit=2)
						user.append(x[1])
						print(user)
						break
						
					else:
						line_count += 1

		
		
		
target = md5_decrypt
target.take_md5()
		
		