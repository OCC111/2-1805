import random
import time
list1 = []

class msg():
	def __init__(self):
		pass
	def sendmsg(self):
		money = int(input('请输入您的资产金额:'))
		if money > 10000:
			print('欢迎您，官二代')
		else:
			print('余额不足')
			time.sleep(2)
			print('即将跳转到充值界面~')
			user = int(input('输入您要充值的金额:'))
			list1.append(user)
			time.sleep(1)
			if user == 0:
				print('想啥呢！你家0元能充值啊！！！！！！go out！')
			else:
				print('充值成功%d'% user)
				time.sleep(1)
				print('即将为您跳转到')
	


			
	
m = msg()
m.sendmsg()
