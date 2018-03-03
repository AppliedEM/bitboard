#!/usr/bin/python

"""
This masterpiece was crafted by the humble yet awesome Michael van Dyk on 02/27/18
Please note that one or two variable names may be NSFW
"""
import requests

book_address = '1Dorian4RoXcnBv9hnQ4Y2C1an6NJ4UrjX' #for test purposes only
testnet_address = 'n2A6fCimAFPzC3SektLU4FnNd1qtbQjqZe'#for test purposes only
bad_tx_hash = '010000000151c477962da1d16ad31df14997c4aea28bec2e7b21c79d282b6cc97bd5e913a2000000006c493046022100ee63741119070cadb66733e9c145307d5cdbe63a4be52967a78f0c37320b1d27022100e8505862023c8129c0e803f71ef8831799920e2ab46d106edc1818b3ce3c9cb801210275b389cfa33cd4b1c1e19a63f03bdffae6e076d2f12c6ab3c13da00676a0ddd2ffffffff0238a78207000000001976a914e268e3825ccbb8b249e426257628e4b3e766f6c588aca8763b00000000001976a914735cf19a695a50c8ac2f9aceec0a3682c3b0153888ac00000000'
smartbit_main_tx_hash = '020000000001014a937af8676310374b31975612993dbb69d9d62bd77d94f3867876d297ff1b2e010000001716001437de5da24ea7c8a3122ff93038f95492bd3834e5feffffff02409c00000000000017a914c0df51d1c3c0a3616627311212a8cf38038aa7fc873dcbe62a0100000017a914050e9b73041b548fc5c0102c08177fb3285ad59b8702483045022100cb851aca4ab0e2b6ad7794a7a35aafaf7193554444156f9eabea726aa71a2689022068bdf09a9b6f10880c8be8895622c308eadfefdf0849b4688a95dbe16d757a8d0121036f4dd476664e417eab722cf99a991c471d38a6a7562275be1bc2dc9a606b468d2dcd0700'
api_mainnet = "https://api.smartbit.com.au/v1/"
api_testnet = "https://testnet-api.smartbit.com.au/api/"
push_suburl = "blockchain/pushtx/"
decode_suburl = "blockchain/decodetx/"

"""
in order to transact
key = 'hex'
value is the hash
then str(usedict).replace("'","\"")
"""
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
		return solicitation.content.decode('utf-8','ignore')

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
	global book_address
	global testnet_address
	hi = grab_utxos(book_address,False) #address corresponds to bitcoin book
	bye = grab_utxos(testnet_address,True) #address from Ryan; only applies to testnet

	assert(type(hi) == dict)
	assert(type(bye) == dict)
	assert(grab_utxos(book_address,True)=='Invalid Bitcoin Address')
	assert(grab_utxos(testnet_address,False)=='Invalid Bitcoin Address')
	assert(sum_utxos(hi) == 101010)
	assert(sum_utxos(bye)==260000000)
	assert(find_bigga_dolla(hi,1000) == 'dbb3853afdb127cb7555bf44a033fa69b57335720132b8c016239ca80e4e570b')
	assert(find_bigga_dolla(hi,202020) == False)

if __name__ == "__main__":
	runtests()
