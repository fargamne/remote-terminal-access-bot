import pymongo

class Userdata:
	def __init__(self, user_id):
		self.user_id = user_id
		self.client = pymongo.MongoClient('localhost', 27017)
		self.db = self.client.remote_access_bot_db
		self.users = self.db.users


	def create(self):
		self.users.update_one({"user_id": self.user_id}, {"$set":{"user_id": self.user_id}}, upsert=True)

	def find(self):
		result = self.users.find_one({"user_id": self.user_id})
		return result

	def update(self):
		result = self.users.update_one({
			"user_id": self.user_id
			}, {
			"$set": {
			"rsa_key": self.rsa_key,
			"ip": self.ip,
			"timestamp": self.timestamp
			}
		} , upsert=False)
		return result

	def delete(self):
		self.users.delete_one({"user_id": self.user_id})
		return True