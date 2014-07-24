from getDoge import *
from getCoin import *

raw_input("What would you like to do?\n1. Just Show Me The Ticker\n2. Specify ")


coin = str(raw_input("Choose a coin:\n1. DogeCoin\n2. BitCoin\n "))

currency = raw_input("What currency would you like?\n1. USD \n2. CAD\n")

amount = float(raw_input("How much would you like the value of? (Enter a numeric value, no currency symbol)"))


if coin == '1':
    coinPrint = "Doge"
elif coin == '2':
    dcoinPrint = "BTC"

if currency == '1':
    currencyPrint = "USD"

print "The current value of ", amount, coinPrint, "is", 
    getCoin().getValue('1', currency, amount), currencyPrint