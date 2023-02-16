import httpx as httpx
import requests
import json
from pymongo import MongoClient
import os
import pymongo
import asyncio


r = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu/")
req = r.json()
#print(req['abilities'])

for ability in req.get('abilities'):
    print(ability)

#for key in req:
#    print(key)

#print(req["abilities"]["ability"][0]["name"])


mongo_client = MongoClient(host=['mongodb+srv://admin:%40Murillo1@requestsdb.jl5lfiv.mongodb.net/test'], document_class=dict, tz_aware=False, connect=True)
mydb = mongo_client['orders']
information = mydb.orders
#for information in information.find():
#    print(information)

x = information.aggregate([
    {
    '$match': {
        'codigoPedido': 1
        }
    },{
    '$project': {
        '_id' : False,
        'codigoPedido': '$codigoPedido'
        }
}
])

y = 0
for i in x:
    x = json.dumps(i, indent = 4)
    y = x
   #print(x)

print(y)
#response = requests.post('link',json=y)

os.environ['NO_PROXY'] = '127.0.0.1'





#q = requests.post("http://127.0.0.1:3000/tema", json={
#    "tema":"Zoonoses"
#})

dsmed = requests.get("http://127.0.0.1:3000/tema")
dsmed = dsmed.json()
#z = json.dumps(dsmed)
#print(z.dumps())

for key in dsmed:
    print(key['tema'])

#print(q)



sem = asyncio.Semaphore(30)

async def get_data(client, postdata):
    async with sem:
        res = client.post(url=_url, data=postdata)
    return res


async def parse_res(client, postdata):
    res = await get_data(client, postdata)
    #if bool(json.loads(res.text)['suggestions']):
    #    _oks = <...grab some JSON fields...>
    #else:
    #    _oks = {}
    return res


async def main(_jobs: int):
    async with httpx.AsyncClient() as client:
        postdata = '{"tema":"Zoonoses"}'
        calls = [
            asyncio.create_task(parse_res(client, postdata))
            for _ in range(_jobs)
        ]

        return await asyncio.gather(*calls)

 # no. of simultaneous requests
_url = "http://127.0.0.1:3000/tema"


