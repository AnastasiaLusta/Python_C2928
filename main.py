def happy(func):
	def wrapper():
		print('I am happy')
		func()
	return wrapper
# Добавить 10 декораторов, которые будут описывать человека (внешность, характер, работа)
	
@happy
def human():
	print('I am human')
	
human()
# import time
# import requests
# def timer(func):
# 	def wrapper():
# 		start = time.time()
# 		func()
# 		end = time.time()
# 		print('Time: ', end-start)
# 	return wrapper

# def logging(func):
# 	def wrapper():
# 		func()
# 		print('Function worked')
# 	return wrapper

# count = 0
# def counter(func):
# 	def wrapper():
# 		global count
# 		count += 1
# 		func()
# 		print('Count:', count)
# 	return wrapper

# @counter
# @logging
# @timer
# def web():
# 	page = requests.get('https://github.com/AnastasiaLusta/Python_C2928')
# 	print(page.text)

# web()
# web()
# web()
# def decor(func):
# 	def wrapper():
# 		print('This is my decorator')
# 		func()
# 		print('The end of my decorator')
# 	return wrapper

# @decor
# def f1():
# 	print('I am function!')

# @decor
# def f2():
# 	print('Hello')

# f1()
# f2()












# try:
# 	a = int(input('A: '))
# 	sign = input('Sign: ')
# 	b = int(input('B: '))
# 	if sign == '/' and b == 0:
# 		raise ZeroDivisionError
# 	if sign != '+' and sign != '-' and sign!='*' and sign!='/':
# 		raise Warning
# 	elif sign == '+':
# 		print(f"{a} + {b} = {a+b}")
# except ValueError:
# 	print('You need to input digits!')
# except ZeroDivisionError:
# 	print('Go to school')
# except Warning:
# 	print('Unknown sign')
# except:
# 	print('Error!')
# # 1) В начале спросить пользователя, как его зовут (предусмотреть все исключительные ситуации)
# # 2) Добавить остальные знаки
# # 3) Если в процессе должны возникнуть какие-то исключительные ситуации, то их тоже обработать












# class Human:
# 	def __init__(self, name):
# 		self.name = name
# 		self.age = 0
# 		self.weight = 0
# 		self.height = 0
# 	def live(self):
# 		print(self.name,' is living')

# class Woman(Human):
# 	def __init__(self, name):
# 		super().__init__(name)
# 		self.money = 0
# 	def live(self):
# 		super().live()
# 		print('lives')
# 	def cook(self):
# 		print('cooks')

# # Если мы в скобках указываем другой класс, то это означает, что мы создаем новый на основе уже существующего. В данном случае мы создаем Woman на основе Human. Это означает, что все характеристики и поведения, которые есть в Human скопируются в Woman. 
# class Woman(Human):
# 	def __init__(self, name):
# 		super().__init__(name)
# 		self.beauty = 0
# # Если нам нужно заменить поведение, то мы повторяем название поведения. И указываем новое.
# 	def live(self):
# 		super().live()
# # Если мы хотим, чтобы сработало поведение базового класса (Human) в классе наследнике и при этом дополнилось. То мы используем super() и дальше прописываем дополнительное поведение
# 		print('Day of',self.name,'life')
# 	def cook(self):
# 		print('Woman is cooking')

# class Man(Human):
# 	def __init__(self, name):
# 		super().__init__(name)
# 		self.strength = 0
# 	def live(self):
# 		super().live()
# 		print('Another live')
# 	def work(self):
# 		print('Man is working')
		
# # Создать базовый класс животное. От него создать наследников Собака, Котик, Хомяк. У базового класса должно быть минимум 2 характеристики и 2 поведения. В классах наследниках добавить 1 дополнительную характеристику и 1 дополнительное поведение.
# obj1 = Human('Human')
# obj1.live()
# obj2 = Woman('Linda')
# obj2.live()
# obj2.cook()
# # obj2.work()
# obj3 = Man('John')
# obj3.live()
# obj3.work()
# # from random import randint
# # class Student:
# # 	def __init__(self, name):
# # 		self.name = name
# # 		self.gladness = 0
# # 		self.progress = 0
# # 		self.money = 0
# # 		self.alive = True
# # 	def education(self, University):
# # 		print(self.name, 'is studying in', University.title)
# # 	def work(self):
# # 		self.money += 50
# # 		self.progress -= 5
# # 		print('Work time')
# # 	def study(self):
# # 		self.progress += 20
# # 		self.gladness -= 10
# # 		print('Study time')
# # 	def chill(self):
# # 		self.gladness += 35
# # 		self.progress -= 8
# # 		print('Chill time')
# # 	def sleep(self):
# # 		self.gladness += 4
# # 		print('Sleep time')
# # 	def say_hello(self):
# # 		print('Hello!')
# # 	def live(self):
# # 		live_cube = randint(1,4)
# # 		if live_cube == 1:
# # 			self.study()
# # 		elif live_cube == 2:
# # 			self.chill()
# # 		elif live_cube == 3:
# # 			self.sleep()
# # 		elif live_cube == 4:
# # 			self.say_hello()
# # 		elif live_cube == 5:
# # 			self.work()
# # 		self.final()
# # 	def final(self):
# # 		if self.progress == 100:
# # 			print('Amazing! You graduated!')
# # 			self.alive = False
# # 		elif self.progress < -20:
# # 			print('Too bad... You are stupid')
# # 			self.alive = False
# # 		elif self.gladness < -20:
# # 			print('Depression :(')
# # 			self.alive = False

# # class University:
# # 	def __init__(self, title):
# # 		self.specialization = 'None'
# # 		self.address = 'None'
# # 		self.title = title
# # 		self.descriptopn = 'None'
# # 	def study(self, Student):
# # 		print(Student.name, 'is studying')
# # 	def pay_for_study(self, Mother):
# # 		print(Mother.name,'paid for study')

# # class Mother:
# # 	def __init__(self, name):
# # 		self.name = name
# # 	def argue(self):
# # 		print("I'm angry!!!")
		
# # print('Bob\'s life')
# # obj1 = Student('Bob')
# # for i in range(365):
# # 	if obj1.alive == False:
# # 		break
# # 	obj1.live()
# # # Создать классы Питомец и Владелец Питомца. Добавить им какие-то взаимодействия друг с другом
# # # Добавить зоомагазин. У Владельца появляется поведение Работать и Деньги. В Зоомагазине при наличии 10 монет можно купить корм. Если не хватает, то сообщаем об этом владельцу
# # print('Jane\'s life')
# # obj2 = Student('Jane')
# # for i in range(365):
# # 	if obj2.alive == False:
# # 		break
# # 	obj2.live()

# # univer = University('Oxford')
# # univer.study(obj2)
# # obj2.education(univer)

# # mom = Mother('Chloe')
# # mom.argue()
# # univer.pay_for_study(mom)