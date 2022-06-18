# password = 'a123456'
password = 'a123456'
number = 3
while number > 0:
	pwd = input('plz input user code: ')
	if pwd == password:
		print('login successful')
		break
	else:
		number -= 1
		print(number ,'times remaining')