class Dog():
	__instance = None
	def __init__(self):
		print("init")
		self.name = "tom"
	
	def __str__(self):
		print("str")
		return "哈哈"

	def __del__(self):
		print("del")

	def __new__(cls):
		print("new")
		if cls.__instance != None:
			return cls.__instance
		else:
			cls.__instance = object.__new__(cls)
		return cls.__instance

dog = Dog()
print(dog)

dog1 = Dog()
print(dog1)
