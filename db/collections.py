from pymongo import MongoClient
from pymongo.collection import Collection

_client = MongoClient(
    host='127.0.0.1',
    port=27017,
)

_db = _client.appointments_db

# Collections
services: Collection = _db.services
appointments: Collection = _db.appointments
clients: Collection = _db.clients
employers: Collection = _db.employers

# Sub-collections
managers: Collection = employers.managers
masters: Collection = employers.masters
