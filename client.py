from telethon import TelegramClient, sync
from config import keys
import time
import os


class Client:
	def __init__(self):
		self.client = TelegramClient(keys['user'], keys['ID'], keys['HASH'])
		self.bot_name = keys['bot_name']
		self.bot_entity = str()
		self.pipe = os.popen("cd ~")
		self.msg_id = 0

	def get_new_message(self):
		msg_iter = self.client.iter_messages(self.bot_entity)
		msg_obj = next(msg_iter)
		return msg_obj

	def execute(self, msg):
		cmd = msg.message
		if "cd" in cmd:
			try:
				out = os.chdir(' '.join(cmd.split(' ')[1:]))
			except FileNotFoundError:
				out = 'Oooops'
		else:
			out = os.popen(cmd + ' 2>&1').read()
		msg.message += '\n'
		msg.message += out if out else "Done"

	def set_entity(self):
		self.bot_entity = self.client.get_entity(self.bot_name)

	def serve(self):
		while True:
			msg = self.get_new_message()
			if msg.id == self.msg_id:
				time.sleep(1)
				continue
			self.msg_id = msg.id
			self.execute(msg)
			msg.edit(msg.message)

	def start(self):
		self.client.start()
		self.set_entity()
		self.serve()

if __name__ == "__main__":
	cli = Client()
	try:
		cli.start()
	except KeyboardInterrupt:
		print("\rTerminate")
