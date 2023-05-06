import masedb
from masedb.find import find_data
from masedb.insert import insert_data
from masedb.update import update_data
from masedb.delete import delete_data
from config import url
import asyncio

#--------------------------------------------------------------------------------------------------------------------------------------------------------

#await find_data(url=url.uri, DatabaseName=DatabaseName, CollectionName=CollectionName, param={'name': 'mark'})
#await insert_data(url=url.uri, DatabaseName=DatabaseName, CollectionName=CollectionName, param={'name': 'mark'})
#await update_data(url=url.uri, DatabaseName=DatabaseName, CollectionName=CollectionName, param1={'name': 'mark'}, param2={'$set':{'let': 10}})
#await delete_data(url=url.uri, DatabaseName=DatabaseName, CollectionName=CollectionName, param={'cash': 10})

#--------------------------------------------------------------------------------------------------------------------------------------------------------

#     Название базы данных и колекции

DatabaseName = 'pondb2'
CollectionName = 'poncoll2'

#--------------------------------------------------------------------------------------------------------------------------------------------------------

async def test():

	db = await find_data(url=url.uri, DatabaseName=DatabaseName, CollectionName=CollectionName, param={'name': 'mark'})
	print(db)

	if not db:
		print('занесение')

		return await insert_data(url=url.uri, DatabaseName=DatabaseName, CollectionName=CollectionName, param={'name':'mark'})

	try: cash = db['cash']
	except: cash = None

	await delete_data(url=url.uri, DatabaseName=DatabaseName, CollectionName=CollectionName, param={'cash': 10})

	if not cash:
		print('update data')
		return await update_data(url=url.uri, DatabaseName=DatabaseName, CollectionName=CollectionName, param1={'name':'mark'}, param2={'$set':{'cash': 10}})

	print(cash)

asyncio.run(test())
