# password = 'a123456'
number = 3
while True:
	code = input('plz input user code: ')
	number -= 1
	print('還剩下', number ,'次機會')
	if code == 'a123456':
		print('登入成功')
		break
	if number <= 0:
		break