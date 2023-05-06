import masedb
from . import connect
import motor.motor_asyncio
import asyncio

async def update_data(url=None, DatabaseName=None, CollectionName=None, param1=None,param2=None):

	if not url:

		return print('[Mase-DB] Не указана ссылка-uri монго дб')

	if not DatabaseName:

		return print('[Mase-DB] Не указано название базы данных монго дб')

	if not CollectionName:

		return print('[Mase-DB] Не указано название колекции монго дб')

	if not param1:

		return print('not param1')

	if not param2:

		return print('not param2')

	db = await connect_to_database(url=url, DatabaseName=DatabaseName, CollectionName=CollectionName)

	await db.update_one(param1,param2)

	return







