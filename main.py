class Human:
	def __init__(self, name):
		self.name = name
		self.age = 0
		self.weight = 0
		self.height = 0
	def live(self):
		print(self.name,' is living')

# Если мы в скобках указываем другой класс, то это означает, что мы создаем новый на основе уже существующего. В данном случае мы создаем Woman на основе Human. Это означает, что все характеристики и поведения, которые есть в Human скопируются в Woman. 
class Woman(Human):
	def __init__(self, name):
		super().__init__(name)
		self.beauty = 0
# Если нам нужно заменить поведение, то мы повторяем название поведения. И указываем новое.
	def live(self):
		super().live()
# Если мы хотим, чтобы сработало поведение базового класса (Human) в классе наследнике и при этом дополнилось. То мы используем super() и дальше прописываем дополнительное поведение
		print('Day of',self.name,'life')
	def cook(self):
		print('Woman is cooking')

class Man(Human):
	def __init__(self, name):
		super().__init__(name)
		self.strength = 0
	def work(self):
		print('Man is working')
		

obj1 = Human('Human')
obj1.live()
obj2 = Woman('Linda')
obj2.live()
obj2.cook()
obj3 = Man('John')
obj3.live()
obj3.work()
# from random import randint
# class Student:
# 	def __init__(self, name):
# 		self.name = name
# 		self.gladness = 0
# 		self.progress = 0
# 		self.money = 0
# 		self.alive = True
# 	def education(self, University):
# 		print(self.name, 'is studying in', University.title)
# 	def work(self):
# 		self.money += 50
# 		self.progress -= 5
# 		print('Work time')
# 	def study(self):
# 		self.progress += 20
# 		self.gladness -= 10
# 		print('Study time')
# 	def chill(self):
# 		self.gladness += 35
# 		self.progress -= 8
# 		print('Chill time')
# 	def sleep(self):
# 		self.gladness += 4
# 		print('Sleep time')
# 	def say_hello(self):
# 		print('Hello!')
# 	def live(self):
# 		live_cube = randint(1,4)
# 		if live_cube == 1:
# 			self.study()
# 		elif live_cube == 2:
# 			self.chill()
# 		elif live_cube == 3:
# 			self.sleep()
# 		elif live_cube == 4:
# 			self.say_hello()
# 		elif live_cube == 5:
# 			self.work()
# 		self.final()
# 	def final(self):
# 		if self.progress == 100:
# 			print('Amazing! You graduated!')
# 			self.alive = False
# 		elif self.progress < -20:
# 			print('Too bad... You are stupid')
# 			self.alive = False
# 		elif self.gladness < -20:
# 			print('Depression :(')
# 			self.alive = False

# class University:
# 	def __init__(self, title):
# 		self.specialization = 'None'
# 		self.address = 'None'
# 		self.title = title
# 		self.descriptopn = 'None'
# 	def study(self, Student):
# 		print(Student.name, 'is studying')
# 	def pay_for_study(self, Mother):
# 		print(Mother.name,'paid for study')

# class Mother:
# 	def __init__(self, name):
# 		self.name = name
# 	def argue(self):
# 		print("I'm angry!!!")
		
# print('Bob\'s life')
# obj1 = Student('Bob')
# for i in range(365):
# 	if obj1.alive == False:
# 		break
# 	obj1.live()
# # Создать классы Питомец и Владелец Питомца. Добавить им какие-то взаимодействия друг с другом
# # Добавить зоомагазин. У Владельца появляется поведение Работать и Деньги. В Зоомагазине при наличии 10 монет можно купить корм. Если не хватает, то сообщаем об этом владельцу
# print('Jane\'s life')
# obj2 = Student('Jane')
# for i in range(365):
# 	if obj2.alive == False:
# 		break
# 	obj2.live()

# univer = University('Oxford')
# univer.study(obj2)
# obj2.education(univer)

# mom = Mother('Chloe')
# mom.argue()
# univer.pay_for_study(mom)