import time 
def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = (func(*args ,**kwargs))
        end = time.time()
        print(end - start)
        return result
    return wrapper
@timer
def say_hi():
    name=input("enter your name:")
    print("hi" , name)

say_hi()

@timer
def make_list(n):
    return list(range(1, n + 1))
result = make_list(1000000)
print(result[:5])  