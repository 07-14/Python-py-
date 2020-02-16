import time

localtime = time.localtime(time.time())
print(localtime)
print(type(localtime))

print(localtime.tm_year)
print(localtime.tm_mon)
print(time.localtime())
