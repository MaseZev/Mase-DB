import masedb
from masedb.connect import connect_to_database
import motor.motor_asyncio
import asyncio

async def insert_data(url=None, DatabaseName=None, CollectionName=None, param=None):

	if not url:

		print('[Mase-DB] Не указана ссылка-uri монго дб')
		return False

	if not DatabaseName:

		print('[Mase-DB] Не указано название базы данных монго дб')
		return False

	if not CollectionName:

		print('[Mase-DB] Не указано название колекции монго дб')
		return False

	if not param:

		print('not param')
		return False

	db = await connect_to_database(url=url, DatabaseName=DatabaseName, CollectionName=CollectionName)

	await db.insert_one(param)

	return







