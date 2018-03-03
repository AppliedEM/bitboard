#!/usr/bin/python

"""
This masterpiece was crafted by the humble yet awesome Michael van Dyk on 02/27/18
Please note that one or two variable names may be NSFW
"""
import requests
import json
import pprint

def grab_utxos(address,on_testnet): # Bitcoin address
	block_info_url = "https://blockchain.info/unspent?active="
	testnet_url = "https://testnet.blockchain.info/unspent?active="
	if on_testnet == True:
		solicitation = requests.get(testnet_url + address)
	else:
		solicitation = requests.get(block_info_url + address)
	try:
		return solicitation.json()
	except:
		return solicitation.content

def sum_utxos(utxo_dict):
	johns_bill = 0
	for ticket in utxo_dict['unspent_outputs']:
		johns_bill+=ticket['value']
	return johns_bill #note this is measured in satoshi, not BTC

def find_bigga_dolla(utxo_dict, price):
	for ticket in utxo_dict['unspent_outputs']:
		if ticket['value'] > price:
			return ticket['tx_hash']
	return False
def runtests():
	hi = grab_utxos('1Dorian4RoXcnBv9hnQ4Y2C1an6NJ4UrjX',False) #address corresponds to bitcoin book
	bye = grab_utxos('n2A6fCimAFPzC3SektLU4FnNd1qtbQjqZe',True) #address from Ryan; only applies to testnet

	assert(type(hi) == dict)
	assert(type(bye) == dict)
	assert(grab_utxos('1Dorian4RoXcnBv9hnQ4Y2C1an6NJ4UrjX',True)=='Invalid Bitcoin Address')
	assert(grab_utxos('n2A6fCimAFPzC3SektLU4FnNd1qtbQjqZe',False)=='Invalid Bitcoin Address')
	assert(sum_utxos(hi) == 101010)
	assert(sum_utxos(bye)==260000000)
	assert(find_bigga_dolla(hi,1000) == 'dbb3853afdb127cb7555bf44a033fa69b57335720132b8c016239ca80e4e570b')
	assert(find_bigga_dolla(hi,202020) == False)

if __name__ == "__main__":
	dat = grab_utxos('n2A6fCimAFPzC3SektLU4FnNd1qtbQjqZe',True)
	print(dat)
	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(dat)
