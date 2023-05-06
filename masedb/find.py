import masedb
from . import connect
import motor.motor_asyncio
import asyncio

async def find_data(url=None, DatabaseName=None, CollectionName=None):

	if not url:

		return print('[Mase-DB] Не указана ссылка-uri монго дб')

	if not DatabaseName:

		return print('[Mase-DB] Не указано название базы данных монго дб')

	if not CollectionName:

		return print('[Mase-DB] Не указано название колекции монго дб')

	db = await connect_to_database(url=url, DatabaseName=DatabaseName, CollectionName=CollectionName)

	info = await db.find_one()

	return info







