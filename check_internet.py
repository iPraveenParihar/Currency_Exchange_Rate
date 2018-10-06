import json
import os
import time

def curr_list():

	file = open("demo_file.json","r").read()
	
	parse = json.loads(file)
	print("\n")
	print(file)
	
	
def read():
	print("\n")
	file = open("data.json","r")
	t = time.ctime(os.path.getmtime("data.json"))
	data = file.read()
	parse = json.loads(data)
	rate = parse["rates"]["INR"]
	disclaimer = parse["disclaimer"]
	print(disclaimer)
	print("Time:",t)
	print(rate)
	print("\n")
	curr_list()


read()
