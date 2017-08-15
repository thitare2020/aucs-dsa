import time

current_time = lambda: int(round(time.time() * 1000))

def function1():
    time.sleep(2)

def function2():
    time.sleep(1)

    
start = current_time()
function1()
function2()
end = current_time()

print("Elapse time: %d mil.seconds" % (end-start))
