from storage.storage import InMemoryStorage

kvs = InMemoryStorage()
print(kvs.put("abc", 123))
print(kvs.get("abc"))

