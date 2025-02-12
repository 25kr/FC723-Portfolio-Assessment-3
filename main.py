import math

class MathCore:
	def __init__(self):
		pass
	
	@staticmethod
	def add(a: float, b: float) -> float:
		return a + b
	
	@staticmethod
	def subtract(a: float, b: float) -> float:
		return a - b
	
	@staticmethod
	def multiply(a: float, b: float) -> float:
		return a * b
	
	@staticmethod
	def divide(a: float, b: float) -> float:
		return a / b
	
	@staticmethod
	def sin(a: float) -> float:
		return math.sin(a)
	
	@staticmethod
	def cos(a: float) -> float:
		return math.cos(a)
	
	@staticmethod
	def tan(a: float) -> float:
		return math.tan(a)
	
	@staticmethod
	def arcsin(a: float) -> float:
		return math.acos(a)
	
	@staticmethod
	def arccos(a: float) -> float:
		return math.acos(a)
	
	@staticmethod
	def arctan(a: float) -> float:
		return math.atan(a)
	
	@staticmethod
	def sqrt(a: float) -> float:
		return math.sqrt(a)
	
	@staticmethod
	def square(a: float, b: float) -> float:
		return a**b
	
	@staticmethod
	def log(a: float) -> float:
		return math.log(a)
	
	@staticmethod
	def ln(a: float) -> float:
		return math.log(a, base = math.e)
	
	@staticmethod
	def pi() -> float:
		return math.pi
	
	@staticmethod
	def mod(a: float, b: float) -> float:
		return a % b