import threading
import time
from concurrent.futures import ThreadPoolExecutor

def func(seconds):
    print(f"sleeping for {seconds} sec")
    time.sleep(2)
    print("Thread finished")
    return seconds


def main():
    time1 = time.perf_counter()
    #normal code
    # func(4)
    # func(2)

    time2 = time.perf_counter()
    print(time2 - time1)

    print('\n')
    print('-----------------------------')
    print('\n')
    #using threads
    t1 = threading.Thread(target=func, args=[4])
    t2 = threading.Thread(target=func, args=[2])

    time3 = round(time.perf_counter(), 2)
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    time4 = round(time.perf_counter(), 2)
    print(time4 - time3)


def poolingDemo():
    with ThreadPoolExecutor(max_workers=1) as executor:
        # future1 = executor.submit(func, 4)
        # future2 = executor.submit(func, 5)
        # print(future1.result())
        # print(future2.result())
        l  = [3,5,1,2]
        results = executor.map(func, l)
        for result in results:
            print(result   )


poolingDemo()