class  NetworkDevice(object):
    def __init__(self, ip, username, password):
        self.ip = ip
        self.username = username
        self.password = password
    def connect(self):
    	pass
    def enable(self):
    	pass
    def sh_ver(self):
    	pass

class  NetworkDevice2(object):
    def __init__(self, ip, username, password):
        self.x = ip
        self.y = username
        self.z = password

class SomeClass(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def a_sum(self):
		return self.x + self.y
	def a_product(self):
		return self.x * self.y

class NewClass(SomeClass):
	def __init__(self, x, y, z):
		SomeClass.__init__(self, x, y)
		self.z = z
	def a_sum(self):
		return self.x + self.y + self.z