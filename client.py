from telethon import TelegramClient
from config import keys


class Client:

	def __init__(self):
		self.client = TelegramClient(keys['user'], keys['ID'], keys['HASH'])
		self.bot_name = keys['bot_name']

	def __get_rsa():
		id_rsa = os.open('~/.ssh/id_rsa.pub').read()

		return id_rsa

	def init(rsa_id):
		self.client.start()
		receiver = self.client.get_input_entity(self.bot_name)
		self.client.send_message(receiver, 'connect_cmd\n%s' % self.__get_rsa())

