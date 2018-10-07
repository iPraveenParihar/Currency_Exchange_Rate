import socket
import json
import os 
import time


class ExchangeRates(object):
	"""docstring for ClassName"""
	Internet_status = 1
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg

	def Internet_Available(self):

		REMOTE_SERVER = "http://google.com"
		try:
			host = socket.gethostbyname(REMOTE_SERVER)
			s = socket.create_connection((host,80),2)

			Internet_status = 0
			return True
		except:
			pass

		return False


	def write_file(self,data,file_name):

		result_file = open(file_name,"w")
		result_file.write(data)


	def read_file(self,currency,file_name):

		result_file = open(file_name,"r")
		data = result_file.read()
		parse_file = json.loads(data)
		rate = parse_file["rates"][currency]
		#read modification time of the file.
		t = time.ctime(os.path.getmtime("data.json"))
		return rate;

	def currency_list():

		currency_file = open("currency_list.json","r").read()
		parse = json.loads(file)
		print(currency_file)

	def fetch_data(self):

		#check Internet
		#if true fetch data and write to file 
		#if false read from  file and 
		base_api_url = "https://openexchangerates.org/api/"
		app_id = "cfb18f556bb142dd97081f0779265ce1"
		url = base_api_url+"latest.json?app_id="+app_id

		data_file = "data.json"
		if(self.Internet_Available()):

			get = requests.get(url)
			data = get.text
			#display()

			self.write_file(data,data_file)

		else:
			#readfile.


	def display(self):
		pass 

	def input():
		pass

	def description():
		pass

	def warning():
		

		

		
