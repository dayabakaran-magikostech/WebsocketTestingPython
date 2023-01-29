from time import sleep
import random
from setup import config
from datetime import datetime

def main(instrument):
	instrument_token = instrument['instrument_token']
	print(instrument_token)
	trading_symbol = config['instrumentObj'][instrument_token]['symbol']
	ts = datetime.now()
	counter = config['counter']

	config['counter'] += 1
	print("Got Tick: ", instrument_token, trading_symbol, counter, config['counter'])
	sleep(3)
	print("Execution finished for: ",instrument_token, trading_symbol, counter, config['counter'])
	config['counter'] -= 1

def subscribe():
	rn = random.randint(0, 8)
	refreshInterval = 300 * rn
	sleep(refreshInterval/1000)
	total_instruments = len(config['instruments'])-1
	rn2 = random.randint(0, total_instruments)
	random_instrument = str(config['instruments'][rn2])
	print("Calling main: ",random_instrument)
	main(config['tickObject'][random_instrument])

	subscribe()

subscribe()