import random
def blackjack(var):
	cards = [2,3,4,5,6,7,8,9,10,11,12,13,14,2,3,4,5,6,7,8,9,10,11,12,13,14,2,3,4,5,6,7,8,9,10,11,12,13,14,2,3,4,5,6,7,8,9,10,11,12,13,14,
	]
	card = []
	money = var
	while money >= 20:
		if len(cards) < 10:
			
			print('------------\nDECK SHUFFLE')
			cards = card + cards
			card.clear()
		first = cards.pop(random.randint(0,len(cards)-1))
		card.append(first)
		second = cards.pop(random.randint(0,len(cards)-1))
		card.append(second)
		third = cards.pop(random.randint(0,len(cards)-1))
		card.append(third)
		fourth = cards.pop(random.randint(0,len(cards)-1))
		card.append(fourth)
		print('~~~~~~~~~~~~~~~~~~~~~')
		print('------BLACKJACK------')
		print('~~~~~~~~~~~~~~~~~~~~~')
		print('Funds: $' + str(money) + ' | $10 minimum ')
	
		#betting
		
		bet = input('Press return for min, or make new bet (ex. 20)\n')
		if bet == '':
			bet = 10
		elif bet == 'a':
			bet = money
		elif not bet.isdigit():
			print('Wrong input: Using min bet')
			bet = 10
		elif int(bet) > money:
			print('Insufficent funds, using minimum\n')
			bet = 10
		elif int(bet) < 10:
			print('Less than min, using minimum\n')
			bet = 10
		
		#variables
		
		output = 0
		dealer = 0
		ace = 0
		dace = 0
		win = 'YOU WIN :)'
		lose = 'YOU LOSE :('
		push = 'PUSH'
	
	#shows original cards and dealers face up card
	
		if first == 11:
			first = 'A'
		if first == 12:
			first = 'J'
		if first == 13:
			first = 'Q'
		if first == 14:
			first = 'K'
		if second == 11:
			second = 'A'
		if second == 12:
			second = 'J'
		if second == 13:
			second = 'Q'
		if second == 14:
			second = 'K'
		if third == 11:
			third = 'A'
		if third == 12:
			third = 'J'
		if third == 13:
			third = 'Q'
		if third == 14:
			third = 'K'
		if fourth == 11:
			fourth = 'A'
		if fourth == 12:
			fourth = 'J'
		if fourth == 13:
			fourth = 'Q'
		if fourth == 14:
			fourth = 'K'
			
		print('----------------\n')
		print('Dealer: ' + str(third) + ', (?)')
		print(' ')
		print('Your cards: ' + str(first) + ', ' + str(second))
		
		#giving value to a-j
		
		if first == 'A' :
			first = 11
			ace += 1
		if first == 'K' :
			first = 10
		if first == 'Q' :
			first = 10
		if first == 'J' :
			first = 10
		if second == 'A' :
			ace += 1
			second = 11
		if second == 'K' :
			second = 10
		if second == 'Q' :
			second = 10
		if second == 'J' :
			second = 10
		if third == 'A' :
			third = 11
			dace += 1
		if third == 'K' :
			third = 10
		if third == 'Q' :
			third = 10
		if third == 'J' :
			third = 10
		if fourth == 'A' :
			fourth = 11
			dace += 1
		if fourth == 'K' :
			fourth = 10
		if fourth == 'Q' :
			fourth = 10
		if fourth == 'J' :
			fourth = 10
			
		output = first + second
		if output > 21:
			output -= 10
			ace -= 1
		print('Value: ' + str(output))
		print('')
	#Now you can hit
		while output < 21 :
			if int(third) + int(fourth) == 21:
				print('Dealer Blackjack :(')
				break
			hit = input('hit(h) or stay(s)?\n')
			if hit == 'h':
				rand = cards.pop(random.randint(0,len(cards)-1)) 
				if rand == 11 and int(output) + 11 > 21:
					output += 1
					i = 'A'
				elif rand == 11:
					i = 'A'
					output += 11
					ace += 1
				elif rand == 12:
					i = 'J'
					output += 10
				elif rand == 13:
					i = 'Q'
					output += 10
				elif rand == 14:
					i = 'K'
					output += 10
				elif rand >= 2 or rand <= 10:
					output += rand
					i = str(rand)
				if ace > 0 and output > 21:
					output -= 10
					ace -= 1
				card.append(rand)
				print(str(i) + ' --> ' + str(output))
			if hit == 's':
				break
		print(' ')
		final= "Your Final = "
		print(final + str(output) + '\n')
	#dealers hitting option automated
		dealer += int(third) + int(fourth)
		if int(third) + int(fourth)  == 22:
			dealer -= 10
			dace -= 1
		print('Dealer: ' + str(third) + ', '  + str(fourth) + ' = ' + str(dealer))
		while dealer <= 16 :
			if dealer > 21:
				break
			if dealer == 21:
				break
			rando = cards.pop(random.randint(0,len(cards)-1)) 
			if rando == 11 and int(dealer) + 11 > 21:
				dealer += 1
				x = 'A'
			elif rando == 11:
				x = 'A'
				dealer += 11
				ace += 1
			elif rando == 12:
				x = 'J'
				dealer += 10
			elif rando == 13:
				x = 'Q'
				dealer += 10
			elif rando == 14:
				x = 'K'
				dealer += 10
			elif rando >= 2 or rando <= 10:
				dealer += rando
				x = rando
			if dace > 0 and dealer > 21:
				dealer -= 10
				dace -= 1
					
			card.append(rando)
			print(str(x) + ' --> ' +str(dealer))
		print('')
		
	#payouts
		
		if first + second == 21:
			money += int(bet) * 1.5
			print('BLACKJACK!!!')
		elif dealer and output > 21:
			money -= int(bet)
			print(lose)
		elif output > dealer and output <= 21:
			money += int(bet)
			print(win)
		elif output == dealer:
			money += 0
			print(push)
		elif output < dealer and dealer <= 21:
			money -= int(bet)
			print(lose)
		elif dealer > 21 and output <= 21:
			money += int(bet)
			print(win)
		else: 
			money -= int(bet)
			print(lose)
		print('')
	if money < 10:
		return 'Not enough money!! Goodbye'


print(blackjack(1000))



