import random
r = random.randint(1, 100)
while True:
	num = input('請猜數字:')
	num = int(num)
	if num == r:
		print('恭喜答對!')
		break
	elif num < r:
		print('比答案小')
	elif num > r:
		print('比答案大')
		