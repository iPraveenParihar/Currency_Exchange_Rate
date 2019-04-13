import sys

#Required python libraries 
try:
	import json
	import os 
	import time
	import requests
	import datetime
	import socket
except Exception as e:
	print(e)


SERVER = "https://openexchangerates.org" #use www.google.com if not working.
Internet_Status = 0

class ExchangeRates():

	def __init__(self,):
		super(ExchangeRates, self).__init__()
		

	def Internet_Available(self,hostname):

		try:
			host = socket.gethostbyname(hostname)
			s = socket.create_connection((host,80),2)
			return True

		except Exception as e:
			print(e)

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

	def ErrorStatus(self,error_file):
		
		error_status = error_file["status"]
		msg = error_file["message"]
		desp = error_file["description"]

		print(msg)
		print(desp)


	def fetch_data(self):

		#check Internet
		#if true fetch data and write to file 
		#if false read from  file and 
	
		os.system("clear")

		base_api_url = "https://openexchangerates.org/api/"
		app_id = "cfb18f556bb142dd97081f0779265ce1"
		url = base_api_url+"latest.json?app_id="+app_id
		data_file = "data.json"
		
		#Check for required files..
		try:
			test = open(data_file,"r")
			test1 = open("currency_list.json","r")
		except FileNotFoundError as e:
			print(e)
			sys.exit()

		try:

			if(self.Internet_Available(SERVER)):
				Internet_Status = 1
			else:
				Internet_Status = 0

			if(Internet_Status == 1	):

				get = requests.get(url)
				data = get.text
				parse_file = json.loads(data)

				for key in parse_file.keys():
					if key == "error":
						self.ErrorStatus(parse_file)
						sys.exit()

				self.description(1)
				self.write_file(data,data_file)
				

				while(1):
					currency_input = self.Input()

					if(self.check_currency(currency_input)):
						exchange_rate = parse_file["rates"][currency_input]
						print(("1 USD = %.3f %s")% (exchange_rate,currency_input))
						if(currency_input == 'USD'):
							continue
						print(("1 %s = %.3f USD")% ( currency_input, 1/exchange_rate))

			else:
				self.description(0)
				while(1):
					currency_input = self.Input()

					if(self.check_currency(currency_input)):
						exchange_rate , time = self.read_file(currency_input,data_file)
						print(("1 USD = %.3f %s")% (exchange_rate,currency_input))
						if(currency_input == 'USD'):
							continue
						print(("1 %s = %.3f USD")% ( currency_input, 1/exchange_rate))

		except NameError as e:
			print(e)
		except AttributeError as e:
			print(e)
		except KeyError as e:
			print(e)
		except ValueError as e:
			print(e)
		except IOError as e:
			print(e)
		sys.exit()

	def Input(self):
		currency_input = input("You have:").upper()
		
		if(currency_input == 'Q'):
			os.system("clear")
			sys.exit()
		elif(currency_input == 'C'):
			self.currency_list()
		elif(currency_input == "CLEAR"):
			os.system("clear")
		else:
			return currency_input

	def description(self,status):
		
		if(status == 1):
			time = 	datetime.datetime.now()
			time = time.strftime("%c")
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
#Invoking main module 
object.fetch_data()

		
		
