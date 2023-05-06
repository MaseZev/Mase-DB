import masedb
from masedb.find import find_data
from masedb.insert import insert_data
from masedb.update import update_data
from config import url
import asyncio

#await find_data(url=url.uri, DatabaseName=DatabaseName, CollectionName=CollectionName)
#await insert_data(url=url.uri, DatabaseName=DatabaseName, CollectionName=CollectionName, param={'name': 'mark'})
#await update_data(url=url.uri, DatabaseName=DatabaseName, CollectionName=CollectionName, param1={'name': 'mark'}, param2={'$set':{'let': 10}})

DatabaseName = 'pondb2'
CollectionName = 'poncoll2'


async def test():

	db = await find_data(url=url.uri, DatabaseName=DatabaseName, CollectionName=CollectionName)
	print(db)
	try: 
		cash = db['cash']
	except:
		await insert_data(url=url.uri, DatabaseName=DatabaseName, CollectionName=CollectionName, param={'cash': 19})
		cash = 'Успешное занесение'

	print(cash)



asyncio.run(test())
