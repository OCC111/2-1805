class fang():
	def __init__(self,name,price):
		self.name = name
		self.price = price
	def __str__(self,name,price):
		msg = '我是%s,%d元!'
		return msg

laowang = fang('约翰逊',6000000000000)
print(laowang)
