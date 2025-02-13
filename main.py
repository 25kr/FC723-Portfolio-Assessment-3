import math

class MathCore:
	def __init__(self):
		pass
	
	@staticmethod
	def add(a: float, b: float) -> float:           #add(a+b)
		return a + b
	
	@staticmethod
	def subtract(a: float, b: float) -> float:      #subtract(a-b)
		return a - b
	
	@staticmethod
	def multiply(a: float, b: float) -> float:      #multiply(a*b)
		return a * b
	
	@staticmethod
	def divide(a: float, b: float) -> float:        #divide(a/b)
		return a / b
	
	@staticmethod
	def sin(a: float) -> float:                     #sin(a)
		return math.sin(a)
	
	@staticmethod
	def cos(a: float) -> float:                     #cos(a)
		return math.cos(a)
	
	@staticmethod
	def tan(a: float) -> float:                     #tan(a)
		return math.tan(a)
	
	@staticmethod
	def arcsin(a: float) -> float:                  #sin^-1 (a)
		return math.acos(a)
	
	@staticmethod
	def arccos(a: float) -> float:                  #cos^-1 (a)
		return math.acos(a)
	
	@staticmethod
	def arctan(a: float) -> float:                  #tan^-1 (a)
		return math.atan(a)
	
	@staticmethod
	def sqrt(a: float) -> float:                    #√a
		return math.sqrt(a)
	
	@staticmethod
	def square(a: float, b: float) -> float:        #a^b
		return a**b
	
	@staticmethod
	def log(a: float) -> float:                     #log a
		return math.log10(a)
	
	@staticmethod
	def ln(a: float) -> float:                      # ln a
		return math.log(a, math.e)
	
	@staticmethod
	def pi() -> float:                              #3.1415926...
		return math.pi
	
	@staticmethod
	def mod(a: float, b: float) -> float:           # modular(a%b)
		return a % b