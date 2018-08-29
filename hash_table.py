class Entry(object):
	def __init__(self, key, value, _next = None):
		self.key = key
		self.value = value 
		self.next = _next 


	def __str__(self):
		return  "Key: " +str(self.key) + " " "Value: " + str(self.value)



class HashTable(object):
	def __init__(self, *, hash_function = hash, buckets = 64):
		self.buckets = [[] for _ in range(buckets)]
		self.__hash = lambda x: abs(hash_function(x)) % buckets

	def __setitem__(self, key, value):
		hashed = self.__hash(key)
		bucket = self.buckets[self.__hash(key)]
		if not bucket:
			self.buckets[hashed] = Entry(key, value)
			return
		curr = bucket
		while curr.key != key and curr.next:
			curr = curr.next
		if curr.key == key:
			curr.value = value
		else:
			curr.next = Entry(key, value)
			
	def __getitem__(self, key):
		hashed = self.__hash(key)
		bucket = self.buckets[self.__hash(key)]
		if not bucket:
			raise KeyError
		current = bucket 
		while current.key != key and current.next:
			current = current.next
		if current.key == key:
			return current.value
		else:
			raise KeyError
	def __delitem__(self, key):
		bucket = self.buckets[self.__hash(key)]
		hashed = self.__hash(key)
		if not bucket:
			raise KeyError
		elif bucket.key == key:
			self.buckets[hashed] = bucket.next
			prev = None
			current = bucket
			while current.key != key and current.next:
				prev = current
				current = current.next
			if current.key == key:
				prev.next = current.next
			else:
				raise KeyError

	def print_table(self):
		for pairs in self.buckets:
			print(str(pairs))



			


h = HashTable()
h["conor"] = "123"
h["conor"] = "122"
h["david"] = "3"
print(h["david"])
h.print_table()


