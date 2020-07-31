from random import randint
import hashlib
class Password:
	"""
	Password class
	It is a string, which can mutate
	"""
	def __init___(self):
		self.__password = ''
	
	def clear(self):
		self.__password = ''
	def generateRandom(self, length):
		out = ''
		for _i in range(length):
			out += chr(randint(48,122))
		self.__password = out
	
	def generateMD5(self, seed):
		self.__password = hashlib.md5(str(seed).encode()).hexdigest()
		
	def generateShakeMD5(self, seed):
		self.generateMD5(seed)
		self.shake()
	
	def loopGenMD5(self, seed, loopsValue = 1):
		for _i in range(loopsValue):
			self.generateMD5(seed)
			seed = self.getPassword()
	
	def loopGenShakeMD5(self, seed, loopsValue = 1):
		for _i in range(loopsValue):
			self.generateMD5(seed)
			self.shake()
			seed = self.getPassword()
	
	def generateRandomMD5(self, top = 340282366920938463463374607431768211456):
		seed = randint(0, top)
		self.generateMD5(seed)
	
	def generateSHA256(self, seed):
		self.__password = hashlib.sha256(str(seed).encode()).hexdigest()
	
	def generateShakeSHA256(self, seed):
		self.generateSHA256(seed)
		self.shake()
	
	def generateRandomSHA256(self, top = 115792089237316195423570985008687907853269984665640564039457584007913129639936):
		seed = randint(0, top)
		self.generateSHA256(seed)
	
	def loopGenSHA256(self, seed, loopsValue = 1):
		for _i in range(loopsValue):
			self.generateSHA256(seed)
			seed = self.getPassword()
	
	def loopGenShakeSHA256(self, seed, loopsValue = 1):
		for _i in range(loopsValue):
			self.generateSHA256(seed)
			self.shake()
			seed = self.getPassword()
	
	def generateSHA512(self, seed):
		self.__password = hashlib.sha512(str(seed).encode()).hexdigest()
	
	def generateShakeSHA512(self, seed):
		self.generateSHA512(seed)
		self.shake()
	
	def generateRandomSHA512(self, top = 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084096):
		seed = randint(0, top)
		self.generateSHA512(seed)
	
	def loopGenSHA512(self, seed, loopsValue = 1):
		for _i in range(loopsValue):
			self.generateSHA512(seed)
			seed = self.getPassword()
	
	def loopGenShakeSHA512(self, seed, loopsValue = 1):
		for _i in range(loopsValue):
			self.generateSHA512(seed)
			self.shake()
			seed = self.getPassword()
			
	
	def shake(self):
		temp = list(self.__password)
		self.__password = ''
		while len(temp) > 0:
			charIndex = randint(0, len(temp) - 1)
			charValue = temp[charIndex]
			self.__password += charValue
			temp.pop(charIndex)
	
	def __shakeList(self, inList):
		temp = list(inList) if not isinstance(inList, list) else inList
		inList = []
		while len(temp) > 0:
			elemIndex = randint(0, len(temp) - 1)
			elemValue = temp[elemIndex]
			inList.append(elemValue)
			temp.pop(elemIndex)
			
	def multiShake(self, shakesValue = 1):
		for _i in range(shakesValue):
			self.shake()
			
	def merge(self, *passwords):
		for password in passwords:
			self.__password += password.getPassword()
	
	def mergeShaked(self, *passwords):
		self.__shakeList(passwords)
		for password in passwords:
			self.__password += password.getPassword()
	
	def mergeStrings(self, *strPasswords):
		for strPassword in strPasswords:
			self.__password += strPassword
	
	def cut(self, start='begin', end='end', step=1):
		if start == 'begin' and end == 'end':
			self.__password = self.__password[::step]
		elif start == 'begin':
			self.__password = self.__password[:end:step]
		elif end == 'end':
			self.__password = self.__password[start::step]
		else:
			self.__password = self.__password[start:end:step]
			
	def insertString(self, string, postion = -1):
		self.__password = self.__password.insert(string, postion)

	def insertPassword(self, password, postion = -1):
		self.__password = self.__password.insert(password.getPassword(), postion)	

	def reverse(self):
		self.__password = self.__password[::-1]
		
	def repeat(self, multiplier):
		self.__password *= multiplier
	def getPassword(self):
		return self.__password
	
	def getPasswordMD5Hash(self):
		return hashlib.md5(self.__password.encode()).hexdigest()
	
	def getPasswordSHA256Hash(self):
		return hashlib.sha256(self.__password.encode()).hexdigest()
	
	def getPasswordSHA512Hash(self):
		return hashlib.sha512(self.__password.encode()).hexdigest()
	
class PasswordList:
	def __init__(self, size = 0):
		self.__list = [Password() for i in range(size)]

	def append(self, password):
		self.__list.append(password)
	
	def merge(self):
		out = ''
		for i in range(len(self.__list)):
			out += self.__list[i].getPassword()
		return out
	
	def innerMerge(self):
		cached = self.__list
		self.__list = ['']
		for i in range(len(cached)):
			self.__list[0] += cached[i].getPassword()
	
	def getListElement(self, index):
		return self.__list[index]

	def shake(self):
		temp = self.__list
		self.__list = []
		while len(temp) > 0:
			elementIndex = randint(0, len(temp) - 1)
			elementValue = temp[elementIndex]
			self.__list.append(elementValue)
			temp.pop(elementIndex)


