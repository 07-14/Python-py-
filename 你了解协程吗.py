"""
什么是协程？
又称为微线程、纤程，英文名：Coroutine
import asyncio
async def main():
    print("hello")
    await asyncio.sleep(1)
    print("world")
asyncio.run(main())

通过async/await语法进行声明，是编写异步应用的推荐方式
使用asunc修饰要运行的函数，在运行协程函数时，需要await。

可以用run或者creat_task启动微线程
"""

import asyncio,time

async def say_after(delay,what):
    await asyncio.sleep(delay)
    print(what)

async def fun():
    print(f"开始时间：{time.strftime('%X')}")
    await say_after(1,"hello")
    await say_after(2,"world")
    print(f"执行结束：{time.strftime('%X')}")

asyncio.run(fun())

async def myfun():
    task1 = asyncio.create_task(
        say_after(1,"hello")
    )
    task2 = asyncio.create_task(
        say_after(2,"world")
    )

    print(f"开始时间：{time.strftime('%X')}")
    await task1
    await task2
    print(f"执行结束：{time.strftime('%X')}")

asyncio.run(myfun())