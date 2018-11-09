import socket
import json
import os 
import time
import requests
import sys
import datetime

SERVER = "www.google.com"
Internet_Status = 0

class ExchangeRates():

	def __init__(self,):
		super(ExchangeRates, self).__init__()
		

	def Internet_Available(self,hostname):

		try:
			host = socket.gethostbyname(hostname)
			s = socket.create_connection((host,80),2)

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
	
		return rate,t

	def currency_list(self):

		currency_file = open("currency_list.json","r").read()
		parse_file = json.loads(currency_file)
		print(currency_file)

	def check_currency(self,currency_input):

		currency_file = open("currency_list.json","r").read()
		parse_file = json.loads(currency_file)

		for currency in parse_file:
			if(currency == currency_input):
				return 1

		return 0

	def fetch_data(self):

		#check Internet
		#if true fetch data and write to file 
		#if false read from  file and 
	
		os.system("clear")

		base_api_url = "https://openexchangerates.org/api/"
		app_id = "cfb18f556bb142dd97081f0779265ce1"
		url = base_api_url+"latest.json?app_id="+app_id
		data_file = "data.json"

		if(self.Internet_Available(SERVER)):
			Internet_Status = 1
		else:
			Internet_Status = 0

		self.description()

		if(Internet_Status):

			get = requests.get(url)
			data = get.text
			
			self.write_file(data,data_file)

			parse_file = json.loads(data)

			while(1):
				currency_input = self.Input()

				if(currency_input == 'Q'):
					os.system("clear")
					sys.exit()
				elif(currency_input == 'C'):
					self.currency_list()
				else:
					if(self.check_currency(currency_input)):
						exchange_rate = parse_file["rates"][currency_input]
						print(("1 USD = %.3f %s")% (exchange_rate,currency_input))
						if(currency_input == 'USD'):
							continue
						print(("1 %s = %.3f USD")% ( currency_input, 1/exchange_rate))

		else:
			while(1):
				currency_input = self.Input()

				if(currency_input == 'Q'):
					os.system("clear")
					sys.exit()
				elif(currency_input == 'C'):
					self.currency_list()

				else:
					if(self.check_currency(currency_input)):
						exchange_rate , time = self.read_file(currency_input,data_file)
						print(("1 USD = %.3f %s")% (exchange_rate,currency_input))
						if(currency_input == 'USD'):
							continue
						print(("1 %s = %.3f USD")% ( currency_input, 1/exchange_rate))



	def Input(self):
		currency_input = input("You have:")
		return currency_input.upper()

	def description(self):
		
		if(Internet_Status):
			time = 	datetime.datetime.now()
			time.strftime("%d %b %a %I:%M:%S")
		else:
			rate,time = self.read_file("USD","data.json")

		str = """
Currency Exchange Rates from openexchangerates.org
for 150+ world currencies.
Exchange Rates results are produced with base currency as USD."""
		print(str)
		print("Results from %s" % time)
		print("\n")
		print("Press 'q' to Exit, Press 'c' for list of currencies")

#class object 
object = ExchangeRates()
object.fetch_data()

		
