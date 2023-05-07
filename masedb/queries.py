from motor.motor_asyncio import AsyncIOMotorClient
from .exceptions import ConnectDBException

async def update_data(url=None, DatabaseName=None, CollectionName=None, param1=None,param2=None):

	if not url:

		raise ConnectDBException('[Mase-DB] Не указана ссылка-uri монго дб')

	if not DatabaseName:

		raise ConnectDBException('[Mase-DB] Не указано название базы данных монго дб')

	if not CollectionName:

		raise ConnectDBException('[Mase-DB] Не указано название колекции монго дб')

	if not param1:

		raise ConnectDBException('[Mase-DB] not param1')

	if not param2:

		raise ConnectDBException('[Mase-DB] not param2')

	db = await connect_to_database(url=url, DatabaseName=DatabaseName, CollectionName=CollectionName)

	await db.update_one(param1,param2)

	return

async def insert_data(url=None, DatabaseName=None, CollectionName=None, param=None):

	if not url:

		raise ConnectDBException('[Mase-DB] Не указана ссылка-uri монго дб')

	if not DatabaseName:

		raise ConnectDBException('[Mase-DB] Не указано название базы данных монго дб')

	if not CollectionName:

		raise ConnectDBException('[Mase-DB] Не указано название колекции монго дб')

	if not param:

		raise ConnectDBException('[Mase-DB] not param')

	db = await connect_to_database(url=url, DatabaseName=DatabaseName, CollectionName=CollectionName)

	await db.insert_one(param)

	return

async def get_data(url=None, DatabaseName=None, CollectionName=None, find_param = None, find_key_p = None) -> str:

	data = await connect_to_database(url=url, DatabaseName=DatabaseName, CollectionName=CollectionName)

	if not find_param:

		raise ConnectDBException('[Mase-DB] Параметры поиска не указаны пример - {"data": data}')

	if not find_param:

		raise ConnectDBException('[Mase-DB] Ключ поиска не указаны пример - [Ключ]')

	find = await data.find_one(find_param)
	if find == None:

		db = await connect_to_database(url=url, DatabaseName=DatabaseName, CollectionName=CollectionName)

		db.insert_one(find_param)

		print(db)

	find_key = [find_key_p]

	print(find_key)

	return find_key

async def find_data(url=None, DatabaseName=None, CollectionName=None, param=None) -> str:

	if not url:
		raise ConnectDBException('[Mase-DB] Не указана ссылка-uri монго дб')


	if not DatabaseName:
		raise ConnectDBException('[Mase-DB] Не указано название базы данных монго дб')


	if not CollectionName:

		raise ConnectDBException('[Mase-DB] Не указано название колекции монго дб')


	if not param:

		raise ConnectDBException('[Mase-DB] not param')

	db = await connect_to_database(url=url, DatabaseName=DatabaseName, CollectionName=CollectionName)

	info = await db.find_one(param)

	return info

async def delete_data(url=None, DatabaseName=None, CollectionName=None, param=None):

	if not url:

		raise ConnectDBException('[Mase-DB] Не указана ссылка-uri монго дб')

	if not DatabaseName:

		raise ConnectDBException('[Mase-DB] Не указано название базы данных монго дб')

	if not CollectionName:

		raise ConnectDBException('[Mase-DB] Не указано название колекции монго дб')

	if not param:

		raise ConnectDBException('[Mase-DB] not param1')


	db = await connect_to_database(url=url, DatabaseName=DatabaseName, CollectionName=CollectionName)

	await db.delete_one(param)

	return

async def connect_to_database(url=None, DatabaseName=None, CollectionName=None) -> str:

	if not url:

		raise ConnectDBException('[Mase-DB] Не указана ссылка-uri монго дб')

	if not DatabaseName:

		raise ConnectDBException('[Mase-DB] Не указано название базы данных монго дб')

	if not CollectionName:

		raise ConnectDBException('[Mase-DB] Не указано название колекции монго дб')

	pon = f'client.{DatabaseName}.{CollectionName}'

	try:
		client = AsyncIOMotorClient(url)
		db = client[f'{DatabaseName}'][f'{CollectionName}']

	except Exception:

		raise ConnectDBException('[Mase-DB] Невозможно подключиться')

	return db