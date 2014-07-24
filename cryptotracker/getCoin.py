from getDoge import *
class getCoin:
    def getValue(object, coin, currency, amount):
        
#For Coin:
#1 = doge
#2 = BTC

#For Currency:
#1 = USD
#2 = CAD
#3 = GBP

        if coin == '1':
            return getDoge().calcDogeAmount(amount)
            
        elif coin == 'btc':
            print "You chose BTC"
       # else:
        #    print "Sorry, that coin isn't supported. Or you're just being a jerk."
        
            

  