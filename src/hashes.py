import hashlib

n = 1
key = b'my_value'
key2 = 'string'.encode()
key3=b'lunchtime'

for i in range(n):
    print(hash(key))
    print(hashlib.sha3_256(key).hexdigest())

for i in range(n):
    print(hash(key2))
    print(hashlib.sha3_256(key).hexdigest())

index = hash(key) % 8
index2 = hash(key2) % 8
index3 = hash(key3) % 8
print(index)
print(index2)
print(index3)