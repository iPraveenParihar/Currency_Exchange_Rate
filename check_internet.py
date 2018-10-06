import json
import os
import time

def read():

	file = open("data.json","r")
	t = time.ctime(os.path.getmtime("data.json"))
	print("Time:",t)
	data = file.read()
	parse = json.loads(data)
	rate = parse["rates"]["INR"]
	print(rate)

read()