import random
start = input('請輸入隨機數字開始值:')
end = input('請輸入隨機數字結束值:')
start = int(start)
end = int(end)
r = random.randint(start, end)
c = 0 # 猜的次數
while True:
	num = input('請猜數字:')
	num = int(num)
	c += 1 # c = c + 1 的快寫法
	if num == r:
		print('這是你猜的第', c, '次')
		print('恭喜答對!')
		break
	elif num < r:
		print('比答案小')
	elif num > r:
		print('比答案大')
	print('這是你猜的第', c, '次')	