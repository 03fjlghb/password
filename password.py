password = 'a123456'

while True:
	a_password = input('請輸入密碼')
	if a_password == password:
		print('登入成功!')
		break
	else:
		print('密碼錯誤! 還有兩次機會!')
	a_password = input('請輸入密碼')
	if a_password == password:
		print('登入成功!')
		break
	else:
		print('密碼錯誤! 還有一次機會!')
	a_password = input('請輸入密碼')
	if a_password == password:
		print('登入成功!')
		break
	else:
		print('登入失敗!')
		break		