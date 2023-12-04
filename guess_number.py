import random
answer = random.randint(1, 100)
while True:
	guess = input('請猜一個數字: ')
	guess = int(guess)
	if guess > answer:
		print('再小一點')
	elif guess < answer:
		print('再大一點')
	else:
		print('恭喜猜對了')
		break