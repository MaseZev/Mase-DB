import masedb
from masedb.connect import connect_to_database
import motor.motor_asyncio
import asyncio

async def delete_data(url=None, DatabaseName=None, CollectionName=None, param=None):

	if not url:

		return print('[Mase-DB] Не указана ссылка-uri монго дб')

	if not DatabaseName:

		return print('[Mase-DB] Не указано название базы данных монго дб')

	if not CollectionName:

		return print('[Mase-DB] Не указано название колекции монго дб')

	if not param:

		return print('not param1')


	db = await connect_to_database(url=url, DatabaseName=DatabaseName, CollectionName=CollectionName)

	await db.delete_one(param)

	return







