import masedb
from . import connect
import motor.motor_asyncio
import asyncio

async def get_data(url=None, DatabaseName=None, CollectionName=None, find_param = None, find_key_p = None):

	data = await connect_to_database(url=url, DatabaseName=DatabaseName, CollectionName=CollectionName)

	if not find_param:

		return print('[Mase-DB] Параметры поиска не указаны пример - {"data": data}')

	if not find_param:

		return print('[Mase-DB] Ключ поиска не указаны пример - [Ключ]')

	find = await data.find_one(find_param)
	if find == None:

		db = await connect_to_database(url=url, DatabaseName=DatabaseName, CollectionName=CollectionName)

		db.insert_one(find_param)

		print(db)

	find_key = [find_key_p]

	print(find_key)

	return find_key


