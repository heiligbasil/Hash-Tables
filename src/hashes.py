import hashlib

n = 1
key1 = b'my_value'
key2 = 'string'.encode()
key3 = b'lunchtime'

for i in range(n):
    print(hash(key1))
    print(hashlib.sha3_256(key1).hexdigest())

for i in range(n):
    print(hash(key2))
    print(hashlib.sha3_256(key2).hexdigest())

for i in range(n):
    print(hash(key3))
    print(hashlib.sha3_256(key3).hexdigest())

index1 = hash(key1) % 8
index2 = hash(key2) % 8
index3 = hash(key3) % 8
print(index1)
print(index2)
print(index3)
