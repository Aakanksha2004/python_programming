st = b"hello"
print(st[1])
print(id(st))
print(st.decode('UTF-8'))
#k = bytearray(b"Hello")#
k = bytearray([65,66,67,68])
print(k)
k[0] = 66
print(k)
print(k.decode('UTF-8'))