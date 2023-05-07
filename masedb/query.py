from motor.motor_asyncio import AsyncIOMotorClient
from .exceptions import ConnectDBException

class Query:
	"""docstring for ClassName"""
	def __init__(self, db_name=None, coll_name=None, url=None):
		self.db_name = db_name
		self.coll_name = coll_name
		self.url = url

	async def connect(self):

		if not self.url:

			raise ConnectDBException('[Mase-DB] Не указана ссылка-uri монго дб')

		if not self.db_name:

			raise ConnectDBException('[Mase-DB] Не указано название базы данных монго дб')

		if not self.coll_name:

			raise ConnectDBException('[Mase-DB] Не указано название колекции монго дб')

		try:
			client = AsyncIOMotorClient(self.url)
			db = client[f'{self.db_name}'][f'{self.coll_name}']

		except Exception:

			raise ConnectDBException('[Mase-DB] Невозможно подключиться')

		return db

	async def update(self, param1=None, param2=None):
	

		if not self.url:

			raise ConnectDBException('[Mase-DB] Не указана ссылка-uri монго дб')

		if not self.db_name:

			raise ConnectDBException('[Mase-DB] Не указано название базы данных монго дб')

		if not self.coll_name:

			raise ConnectDBException('[Mase-DB] Не указано название колекции монго дб')

		if not param1:

			raise ConnectDBException('[Mase-DB] not param1')

		if not param2:

			raise ConnectDBException('[Mase-DB] not param2')

		db = await Query.connect(self)

		await db.update_one(param1,param2)

		return

	async def find(self, param=None):

		if not self.url:

			raise ConnectDBException('[Mase-DB] Не указана ссылка-uri монго дб')

		if not self.db_name:

			raise ConnectDBException('[Mase-DB] Не указано название базы данных монго дб')

		if not self.coll_name:

			raise ConnectDBException('[Mase-DB] Не указано название колекции монго дб')


		if not param:

			raise ConnectDBException('[Mase-DB] not param')

		db = await Query.connect(self)

		info = await db.find_one(param)

		return info

	async def insert(self, param=None):
	
		if not self.url:

			raise ConnectDBException('[Mase-DB] Не указана ссылка-uri монго дб')

		if not self.db_name:

			raise ConnectDBException('[Mase-DB] Не указано название базы данных монго дб')

		if not self.coll_name:

			raise ConnectDBException('[Mase-DB] Не указано название колекции монго дб')

		if not param:

			raise ConnectDBException('[Mase-DB] not param')

		db = await Query.connect(self)

		await db.insert_one(param)

		return

	async def delete(self, param=None):
		

		if not self.url:

			raise ConnectDBException('[Mase-DB] Не указана ссылка-uri монго дб')

		if not self.db_name:

			raise ConnectDBException('[Mase-DB] Не указано название базы данных монго дб')

		if not self.coll_name:

			raise ConnectDBException('[Mase-DB] Не указано название колекции монго дб')

		if not param:

			raise ConnectDBException('[Mase-DB] not param1')


		db = await Query.connect(self)

		await db.delete_one(param)

		return




		