# @uthor: Shrihan-P 
""" this is a script for decrypt a md5 password on linux from shadow file 
execute this script with root access.
"""
class md5_decrypt:
	
	def __init__():
		pass
	
	def take_md5():
		file = open("/etc/shadow")
		file_readable = file.read()
		print(file_readable)
		
		
target = md5_decrypt
target.take_md5()