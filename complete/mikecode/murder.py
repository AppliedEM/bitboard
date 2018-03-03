#!/usr/bin/python

"""
This masterpiece was crafted by the humble yet awesome Michael van Dyk on 02/27/18
Please note that one or two variable names may be NSFW
"""
import requests

def grab_utxos(fuckmeharderdaddy): # fuckmeharderdaddy = Bitcoin address
	pornyurl = "https://blockchain.info/unspent?active=" # pornyurl means api_url
	sexy_solicitation = requests.get(pornyurl + fuckmeharderdaddy)# = request
	summoned_hooker = sexy_solicitation.json() # summoned_hooker contains a json of the request response, which in this case includes the transaction outputs
	return summoned_hooker	
def sum_utxos(brothel_tickets): #brothel tickets refers to the json of transaction outputs
	johns_bill = 0L
	for ticket in brothel_tickets['unspent_outputs']:
		johns_bill+=ticket['value']
	return johns_bill #note this is measured in satoshi
def find_bigga_dolla(brothel_tickets, hooker_price):	
	for ticket in brothel_tickets['unspent_outputs']:
		if ticket['value'] > hooker_price:
			return ticket['tx_hash']
	return 'gotta get sum bigger bills, brutha'

if __name__ == "__main__":
	hi = grab_utxos('n2A6fCimAFPzC3SektLU4FnNd1qtbQjqZe') #test address used in bitcoin book
	
