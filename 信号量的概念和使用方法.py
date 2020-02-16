"""
信号量：最古老的同步原语之一，实际上是一个计数器。

当资源释放时计数器就会递增，当申请资源时计数器就会递减。
无资源可以申请时（_value = 0）会发生阻塞，通过semaphore.acquire()返回值判断
"""

from threading import BoundedSemaphore

max = 3
semaphore = BoundedSemaphore(max)
print(semaphore._value)
print(semaphore.acquire())
print(semaphore._value)
semaphore.acquire()
print(semaphore._value)
semaphore.acquire()
print(semaphore._value)
# semaphore.acquire(False) #默认是True，是会发生阻塞的
print(semaphore.acquire(False))
# print(semaphore._value)

semaphore.release()
print(semaphore._value)
semaphore.release()
print(semaphore._value)
semaphore.release()
print(semaphore._value)

# semaphore.release()# 会报错
# print(semaphore._value)