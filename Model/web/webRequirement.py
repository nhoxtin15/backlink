
class webRequirement:
	def __init__(self, storedFiled):
		self.storedFiled = storedFiled
		


		loginStart = 0
		loginEnd = 0
		uploadStart = 0
		uploadEnd = 0

		with open(self.storedFiled) as f:
			self.arr = f.readlines()
			for i in range(len(arr)):
				self.arr[i] = self.arr[i].strip()
				if(self.arr[i] == "loginStart\n"):
					self.loginStart = i
				if(self.arr[i] == "loginEnd\n"):
					self.loginEnd = i
				if(self.arr[i] == "uploadStart\n"):
					self.uploadStart = i
				if(self.arr[i] == "uploadEnd\n"):
					self.uploadEnd = i
		
		
		self.__LoginPayLoad = {}
		self.__UploadPayLoad = {}



		

	def getLoginPayLoad(self):
		return self.__LoginPayLoad
					


	def getUploadPayLoad(self):
		return self.__UploadPayLoad

	def initLoginPayLoad(self,startLogin,endLogin):
		arr = self.arr[startLogin:endLogin]
		for i in range(len(arr)):
			pair = arr[i].split(":")
			key = pair[0].strip()
			value = pair[1].strip()
			self.__LoginPayLoad[key] = value if value != "None" else None
		
	def initUploadPayLoad(self,uploadStart,uploadEnd):
		arr = self.arr[uploadStart:uploadEnd]
		for i in range(len(arr)):
			pair = arr[i].split(":")
			key = pair[0].strip()
			value = pair[1].strip()
			self.__LoginPayLoad[key] = value if value != "None" else None

