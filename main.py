import requests
import urllib3
import json
import re 

class ExchangeRates(object):
	"""docstring for ExchangeRates"""

	base_api_url = "https://openexchangerates.org/api/"
	app_id = "cfb18f556bb142dd97081f0779265ce1"
	url = base_api_url+"latest.json?app_id="+app_id

	#API End points -- 
	latest_rates = "latest.json"
	currencies_list = "currencies.json"

	def __init__(self):
		super(ExchangeRates, self).__init__()
		

	def Is_Internet_Available(self):
		
		url = "http://www.google.com/"
		timeout = 5

		try:
			connection = requests.get(url,timeout=timeout)
			return True
		except requests.ConnectionError:
			print("fsfni")
			return False


	def write_file(self,data,file_name):

		result_file = open(file_name,"w")
		result_file.write(data)
	
	def read_file(self,file_name):

		result_file = open(file_name,"r")
		data = result_file.read()

	def currency_list(self):

		url = "https://openexchangerates.org/api/currencies.json"
		response = requests.get(url)
		Currency_list = response.text
		parsed_json = json.loads(Currency_list)

		
		self.write_file(Currency_list,"currency_list.json")


	def fetch_data(self):
		url = "https://openexchangerates.org/api/latest.json?app_id=cfb18f556bb142dd97081f0779265ce1"

		if self.Is_Internet_Available():
			response = requests.get(url)
			data = response.text
			parse = json.loads(data)
			#rate = parse["rates"]["INR"]
			#print(rate)
			self.write_file(data,"data.json")




p = ExchangeRates()
p.fetch_data()
p.currency_list()
		

		
