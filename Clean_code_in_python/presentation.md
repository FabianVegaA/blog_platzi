---
title: "Clean Code in Python"

marp: true
theme: gaia
size: 16:9
paginate: true

backgroundImage: url('https://marp.app/assets/hero-background.jpg')
style: |
  section {
      backgroundColor: white;
  }
---
<style>
h1,h2,h3{
  transition: 1s;
}
h1:hover, h2:hover, h3:hover{
  color:#55a1f3;
  margin-left: 5%;
}
</style>

<style scoped>
h1, h2, h3,  {
    text-align:center;
}
</style>
![](img/python-logo-master-v3-TM-flattened.png)
# Clean Code in Python
### Introduction to asynchronous code

---

# Asynchronous
> The idea behind asynchronous programming is to have parts in our code that are able to suspend so that other parts of our code can run. - Clean Code in Python

![w:1000px h:250px](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fdatadog-prod.imgix.net%2Fimg%2Fblog%2Ftracing-async-python-code%2Ftrace-async-python-hero.png&f=1&nofb=1)

---
# Event loop

Event loop is the core of every asyncio application. Event loops run asynchronous tasks and callbacks, perform network IO operations, and run subprocesses.

This allows us that if happens an I/O operation, the other processes kept running

---
# Syntactic (From Python 3.5)

### Import standard library
```Python
import asyncio
asyncio.run(mycoro(…))
```
---
### A typical coroutine
```Python
async def mycoro(*args, **kwargs):
    # … logic
    await third_party.coroutine(…)
    # … more of our logic
```
### Coroutine object
```Python
result = await mycoro(…) # doing result = mycoro() would be erroneous
```
---

# That is all?

Of Course not, here are examples for everyone!!

- [Speeding Up Python with Concurrency, Parallelism, and asyncio](https://testdriven.io/blog/concurrency-parallelism-asyncio/)
- [Speed Up Your Python Program With Concurrency](https://realpython.com/python-concurrency/)