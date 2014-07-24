import urllib2

url = 'https://www.dogeapi.com/wow/v2/?a=get_info'

class getDoge:
	def getRawFeed(self):
		feed = urllib2.urlopen(url)
		var1 = feed.read()
		return var1
	
#Get current doge Val and return
	def getDollarVal(self):
		rawval = getDoge().getRawFeed()
		removejunk = rawval.split('"doge_usd":')
		singleval  = removejunk[1].split(",")
		oneDoge = float(singleval[0])
		return oneDoge
	    #Get single Value of Doge	
	
#Calculates the single dollar value of doge

	def calcDogeAmount(object, equalTo):
		#print getDoge().getDollarVal()
		amount = equalTo*getDoge().getDollarVal()
		return amount
