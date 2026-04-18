import time

def decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        print(f"fucntion execution time : {round((time.time()-start_time),2)}s")
    return wrapper

@decorator
def loop():
    count = 0
    for i in range(1000000):
        count +=1

loop()