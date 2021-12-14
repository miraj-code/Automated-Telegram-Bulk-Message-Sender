from telethon import TelegramClient
from telethon import errors
import time
import webbrowser
import os

api_id = 1111111
api_hash = 'ccccccccccccccccccccccccccccccccc'

client = TelegramClient('message', api_id, api_hash)

async def main():

	try:
		os.system('color 0A')
		groups = []
		async for dialog in client.iter_dialogs():
			if dialog.is_group and dialog not in groups:
				groups.append([dialog.name, dialog.id])
		print('=================================================================')
		print('                       Your Groups                               ')
		print('=================================================================')
		k = 1
		for i in groups:
			print(f'{k}. {i}')
			k += 1
		print('=================================================================')

		print()

		gr = int(input('Select a group to scrap users to send your message: '))
		print()
		print('Fetching Members ...')
		user = await client.get_participants(groups[gr - 1][0])
		print('Fetching completed! Your message will be sent to those users')
		print()
		print()
		print('=================================================================')
		print('                    Scrapped Users                               ')
		print('=================================================================')
		c = 0
		for i in user:
			print(i.username)
			c += 1
		print(f'=================================================================\n'
			  f'                   Total of {c} Users                            \n'
			  f'=================================================================')

		print()

		hlp = input('Do you want formatting help for your message? (y/n): ')

		if hlp == 'y':
			webbrowser.open('https://tgraph.io/markdown-07-07')
			print()
			message = input('Please write your message: ')
			print()
			ans = input('Are you sure you want to send the message to those users? (y/n): ')
			print()

			if ans == 'y':
				for i in user:
					await client.send_message(i.id, message, parse_mode='md')
					print('Message sent successfully!')
			elif ans == 'n':
				print('Message Sending Aborted')
			else:
				print('Please enter `y` for yes and `n` for no!')
		elif hlp == 'n':
			print()
			message = input('Please write your message: ')
			print()
			ans = input('Are you sure you want to send the message to those users? (y/n): ')

			if ans == 'y':
				for i in user:
					await client.send_message(i.id, message, parse_mode='md')
					print('Message sent successfully!')
			elif ans == 'n':
				print('Message Sending Aborted')
			else:
				print('Please enter `y` for yes and `n` for no!')
		else:
			print('Please enter `y` for yes and `n` for no!')

	except errors.FloodWaitError as e:
		print('Have to sleep for', e.seconds, 'seconds')
		time.sleep(e.seconds)	
	
with client:
	while True:
		x = input('Do you want to send bulk DM-messages? (y/n): ')
		if x == 'y':
			client.loop.run_until_complete(main())
			os.system('cls')
		elif x == 'n':
			break
		else:
			print('Please enter `y` for yes and `n` for no!')

