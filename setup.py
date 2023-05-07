from setuptools import setup
import re

readme = '''<h1 align=center>Mase-DB v1.2.1</h1>
<p align=center>Легкое использование базы данных монгодб.</p>

## Документация

Документация:
 - [docs](https://mase-db.gitbook.io/docs/)

## Установка
```py
# ЕСЛИ УСТНОВЛЕН
pip install --upgrade masedb

# ЕСЛИ НЕ УСТАНОВЛЕН
python3 -m pip install --upgrade masedb
```
## or
```py
pip install masedb
```

## Применение
### Предпосылки
Прежде чем приступить к работе, вам понадобится несколько вещей:
 - Установить нужные для работы библиотеки
 - Так же установить masedb 
 - И понять как это все работает
 
 И так поехали!(жабы топ)

### Примеры
```py
from config import url
from masedb.query import Query
import asyncio

#--------------------------------------------------------------------------------------------------------------------------------------------------------

#client = Query(DatabaseName, CollectionName, url.uri)

#await client.find(param={'name': 'mark'})
#await client.insert(param={'name': 'mark'})
#await client.update(param1={'name': 'mark'}, param2={'$set':{'let': 10}})
#await client.delete(param={'cash': 10})

#--------------------------------------------------------------------------------------------------------------------------------------------------------

#     Название базы данных и колекции

DatabaseName = 'pondb2'
CollectionName = 'poncoll2'


#--------------------------------------------------------------------------------------------------------------------------------------------------------

client = Query(DatabaseName, CollectionName, url.uri)

async def test():

	db = await client.find(param={'name': 'mark'})
	print(db)

	if not db:
		print('занесение')

		return await client.insert(param={'name':'mark'})

	try: cash = db['cash']
	except: cash = None

	await client.delete(param={'cash': 10})

	if not cash:
		print('update data')
		return await client.update(param1={'name':'mark'}, param2={'$set':{'cash': 10}})

	print(cash)

asyncio.run(test())


```


<br>
'''

requirements = ["pymongo","dnspython","motor"]

setup(name='masedb',
      version='1.2.1',
      description='Easy mase-db use mongodb, motor asyncio',
      url='https://github.com/MaseZev/Mase-DB',
      packages=['masedb'],
      license='mit',
      author="MaseZev",
      author_email='csgomanagement1@gmail.com',
      long_description=readme,
      long_description_content_type="text/markdown",
      install_requires=requirements,
      python_requires='>=3.7',
      zip_safe=True)
