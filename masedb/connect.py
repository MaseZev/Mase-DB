import motor.motor_asyncio
import asyncio

async def connect_to_database(url=None, DatabaseName=None, CollectionName=None):

	if not url:

		return print('[Mase-DB] Не указана ссылка-uri монго дб')

	if not DatabaseName:

		return print('[Mase-DB] Не указано название базы данных монго дб')

	if not CollectionName:

		return print('[Mase-DB] Не указано название колекции монго дб')

	pon = f'client.{DatabaseName}.{CollectionName}'

	try:
		client = motor.motor_asyncio.AsyncIOMotorClient(url)
		dbt = client[f'{DatabaseName}']
		db = dbt[f'{CollectionName}']

	except:

		return print('[Mase-DB] Невозможно подключиться')

	return db




